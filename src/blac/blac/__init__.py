#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4



def decode_bytes(src: bytes) -> Tuple[FileContent, Encoding, NewLine]:
    """Return a tuple of (decoded_contents, encoding, newline).

    `newline` is either CRLF or LF but `decoded_contents` is decoded with
    universal newlines (i.e. only contains LF).
    """
    srcbuf = io.BytesIO(src)
    encoding, lines = tokenize.detect_encoding(srcbuf.readline)
    if not lines:
        return "", encoding, "\n"

    newline = "\r\n" if b"\r\n" == lines[0][-2:] else "\n"
    srcbuf.seek(0)
    with io.TextIOWrapper(srcbuf, encoding) as tiow:
        return tiow.read(), encoding, newline


def format_file_in_place(src: Path, mode: Mode) -> bool:
    """Format file under `src` path. Return True if changed.
    `mode` and `fast` options are passed to :func:`format_file_contents`.
    """
    if src.suffix == ".h":
        # mode = replace(mode, is_pyi=True)
		pass

    then = datetime.fromtimestamp(src.stat().st_mtime, timezone.utc)
    header = b""
    with open(src, "rb") as buf:
        src_contents, encoding, newline = decode_bytes(buf.read())

	dst_contents = format_file_contents(src_contents, fast=fast, mode=mode)
