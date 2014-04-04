#  (C) Catchoom Technologies S.L.
#  Licensed under the MIT license.
#  https://github.com/catchoom/catchoom-python/blob/master/LICENSE
#  All warranties and liabilities are disclaimed.

"Default settings"

RECOGNITION_HOSTNAME = 'https://r.catchoom.com'
MANAGEMENT_HOSTNAME = 'https://crs.catchoom.com'

RECOGNITION_API_VERSION = "v1"
MANAGEMENT_API_VERSION = "v0"

USER_AGENT = "Catchoom Python API"

DEFAULT_QUERY_MIN_SIZE = 270  # default image transformation parameters
DEFAULT_IMG_QUALITY = 80  # for jpeg compression, recommended range [75-85]

ALLOWED_IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
ALLOWED_OBJECT_TYPES = ["collection", "item", "image", "token", "media"]
