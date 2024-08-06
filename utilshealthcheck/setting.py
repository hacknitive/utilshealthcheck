from os import (
    sep,
    environ,
)

from pydantic_settings import (
    SettingsConfigDict,
    BaseSettings,
)
from utilscommon import (
    enum,
    schema,
    base_dir_path_finder,
    add_dir_to_env,
    is_test_mode,
    generate_build_versioning,
    create_dir,
)
from utilslogging.prepare_logger import PrepareLogger

# =========================================================================================================== DIRECTORY
BASE_DIR_PATH = base_dir_path_finder(
    file_path=__file__,
    number_of_going_up=2,
)

BASE_DIR_STR = str(BASE_DIR_PATH)

add_dir_to_env(path_=BASE_DIR_STR)

IO_DIR_STR = create_dir(f"{BASE_DIR_STR}{sep}io")

# ============================================================================================================ SETTINGS
env_file_path = BASE_DIR_STR + sep + environ["ENV_FILE"]


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_file_path,
        env_file_encoding='utf-8',
        env_nested_delimiter='__',
        env_ignore_empty=True,
        env_parse_none_str='none',
        env_parse_enums=True,
        extra='ignore',
    )

    GENERAL: schema.SchemaGeneral
    UVICORN_SERVER: schema.SchemaUvicornServer
    LOGGING: schema.SchemaLogging
    GZIP_MIDDLEWARE: schema.SchemaGZipMiddleware


SETTINGS = _Settings()

# ============================================================================================================ RUN MODE
if is_test_mode():
    RUN_MODE = enum.EnumRunMode.test
else:
    if SETTINGS.GENERAL.IS_PRODUCTION:
        RUN_MODE = enum.EnumRunMode.production

    else:
        RUN_MODE = enum.EnumRunMode.development

# ============================================================================================================== LOGGER
prepare_logger_obj = PrepareLogger(
    project_base_dir=IO_DIR_STR,
    **SETTINGS.LOGGING.model_dump(by_alias=True),
)
logger = prepare_logger_obj.perform()

# ============================================================================================================= VERSION
VERSION = generate_build_versioning(
    build_file_address=f"{IO_DIR_STR}{sep}buildnumber.version",
    version=SETTINGS.GENERAL.APPLICATION_VERSION,
)

# ============================================================================================================= VERSION
logger.info("ENV_FILE: %s", env_file_path)
logger.info("Run Mode: %s", RUN_MODE.value)