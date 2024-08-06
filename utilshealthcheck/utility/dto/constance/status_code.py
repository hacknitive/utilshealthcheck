from fastapi import status as _status

HTTP_100_CONTINUE = _status.HTTP_100_CONTINUE
HTTP_101_SWITCHING_PROTOCOLS = _status.HTTP_101_SWITCHING_PROTOCOLS
HTTP_102_PROCESSING = _status.HTTP_102_PROCESSING
HTTP_103_EARLY_HINTS = _status.HTTP_103_EARLY_HINTS

HTTP_200_OK = _status.HTTP_200_OK
HTTP_201_CREATED = _status.HTTP_201_CREATED
HTTP_202_ACCEPTED = _status.HTTP_202_ACCEPTED
HTTP_203_NON_AUTHORITATIVE_INFORMATION = _status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
HTTP_204_NO_CONTENT = _status.HTTP_204_NO_CONTENT
HTTP_205_RESET_CONTENT = _status.HTTP_205_RESET_CONTENT
HTTP_206_PARTIAL_CONTENT = _status.HTTP_206_PARTIAL_CONTENT
HTTP_207_MULTI_STATUS = _status.HTTP_207_MULTI_STATUS
HTTP_208_ALREADY_REPORTED = _status.HTTP_208_ALREADY_REPORTED
HTTP_226_IM_USED = _status.HTTP_226_IM_USED

HTTP_300_MULTIPLE_CHOICES = _status.HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY = _status.HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND = _status.HTTP_302_FOUND
HTTP_303_SEE_OTHER = _status.HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED = _status.HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY = _status.HTTP_305_USE_PROXY
HTTP_306_RESERVED = _status.HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT = _status.HTTP_307_TEMPORARY_REDIRECT
HTTP_308_PERMANENT_REDIRECT = _status.HTTP_308_PERMANENT_REDIRECT

HTTP_400_BAD_REQUEST = _status.HTTP_400_BAD_REQUEST
HTTP_401_UNAUTHORIZED = _status.HTTP_401_UNAUTHORIZED
HTTP_402_PAYMENT_REQUIRED = _status.HTTP_402_PAYMENT_REQUIRED
HTTP_403_FORBIDDEN = _status.HTTP_403_FORBIDDEN
HTTP_404_NOT_FOUND = _status.HTTP_404_NOT_FOUND
HTTP_405_METHOD_NOT_ALLOWED = _status.HTTP_405_METHOD_NOT_ALLOWED
HTTP_406_NOT_ACCEPTABLE = _status.HTTP_406_NOT_ACCEPTABLE
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = _status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED
HTTP_408_REQUEST_TIMEOUT = _status.HTTP_408_REQUEST_TIMEOUT
HTTP_409_CONFLICT = _status.HTTP_409_CONFLICT
HTTP_410_GONE = _status.HTTP_410_GONE
HTTP_411_LENGTH_REQUIRED = _status.HTTP_411_LENGTH_REQUIRED
HTTP_412_PRECONDITION_FAILED = _status.HTTP_412_PRECONDITION_FAILED
HTTP_413_REQUEST_ENTITY_TOO_LARGE = _status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
HTTP_414_REQUEST_URI_TOO_LONG = _status.HTTP_414_REQUEST_URI_TOO_LONG
HTTP_415_UNSUPPORTED_MEDIA_TYPE = _status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = _status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
HTTP_417_EXPECTATION_FAILED = _status.HTTP_417_EXPECTATION_FAILED
HTTP_418_IM_A_TEAPOT = _status.HTTP_418_IM_A_TEAPOT
HTTP_421_MISDIRECTED_REQUEST = _status.HTTP_421_MISDIRECTED_REQUEST
HTTP_422_UNPROCESSABLE_ENTITY = _status.HTTP_422_UNPROCESSABLE_ENTITY
HTTP_423_LOCKED = _status.HTTP_423_LOCKED
HTTP_424_FAILED_DEPENDENCY = _status.HTTP_424_FAILED_DEPENDENCY
HTTP_425_TOO_EARLY = _status.HTTP_425_TOO_EARLY
HTTP_426_UPGRADE_REQUIRED = _status.HTTP_426_UPGRADE_REQUIRED
HTTP_428_PRECONDITION_REQUIRED = _status.HTTP_428_PRECONDITION_REQUIRED
HTTP_429_TOO_MANY_REQUESTS = _status.HTTP_429_TOO_MANY_REQUESTS
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = _status.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = _status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS

HTTP_500_INTERNAL_SERVER_ERROR = _status.HTTP_500_INTERNAL_SERVER_ERROR
HTTP_501_NOT_IMPLEMENTED = _status.HTTP_501_NOT_IMPLEMENTED
HTTP_502_BAD_GATEWAY = _status.HTTP_502_BAD_GATEWAY
HTTP_503_SERVICE_UNAVAILABLE = _status.HTTP_503_SERVICE_UNAVAILABLE
HTTP_504_GATEWAY_TIMEOUT = _status.HTTP_504_GATEWAY_TIMEOUT
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = _status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED
HTTP_506_VARIANT_ALSO_NEGOTIATES = _status.HTTP_506_VARIANT_ALSO_NEGOTIATES
HTTP_507_INSUFFICIENT_STORAGE = _status.HTTP_507_INSUFFICIENT_STORAGE
HTTP_508_LOOP_DETECTED = _status.HTTP_508_LOOP_DETECTED
HTTP_510_NOT_EXTENDED = _status.HTTP_510_NOT_EXTENDED
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = _status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED