import CatFaceCropper
cropper = CatFaceCropper.CatFaceCropper()

# cropper.crop_image("./input/cat1.jpg", True)

cropper.crop_image_dir('./input/male', True)
cropper.crop_image_dir('./input/female', True)

cropper.crop_image_dir('./input/male2', True)
cropper.crop_image_dir('./input/female2', True)

