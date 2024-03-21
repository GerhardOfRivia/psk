# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8


from exif import Image


def print_exif_info(image: Image):
    
    print(dir(image))

    try:
        print(f"Lens make: {image.get('lens_make', 'Unknown')}")
        print(f"Lens model: {image.get('lens_model', 'Unknown')}")
        print(f"Lens specification: {image.get('lens_specification', 'Unknown')}")
        print(f"OS version: {image.get('software', 'Unknown')}\n")

        print(f"316 {image.get('<unknown EXIF tag 316>', 'Unknown')}")
        print(f"322 {image.get('<unknown EXIF tag 322>', 'Unknown')}")
        print(f"323 {image.get('<unknown EXIF tag 323>', 'Unknown')}")
        print(f"42080 {image.get('<unknown EXIF tag 42080>', 'Unknown')}\n")

        print(f"{image.datetime_original}.{image.subsec_time_original} {image.get('offset_time', '')}\n")
        print(f"Latitude: {image.gps_latitude} {image.gps_latitude_ref}")
        
        print(f"Longitude: {image.gps_longitude} {image.gps_longitude_ref}\n")
    except Exception:
        pass


def main():

    with open(f"./images/{image_name}", "rb") as img:
        image = Image(img)

    print_exif_info(image)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logger.exception(err)

