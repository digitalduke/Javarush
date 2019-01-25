import os, platform, logging

if platform.platform().startswith("Linux"):
    log_file = os.path.join(os.getenv("HOME"), "test.log")
else:
    print("Run under Linux, please.")
    exit()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(levelname)s: %(message)s",
    filename = log_file,
    filemode = 'w'
)

logging.info("this is info message");
logging.debug("this is debug message");
logging.warning("this is warning message");

logging.info(platform.python_implementation())
logging.info(platform.python_revision())
logging.info(platform.system())
logging.info(platform.uname())
