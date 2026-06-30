import logging

def setup_logging():
    #配置全局日志
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

#预置一个应用级别的logger
logger = logging.getLogger("app")