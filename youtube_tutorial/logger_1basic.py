import logging 

def main() -> None:
    #     logging.basicConfig(level=logging.WARNING)
    #     logging.basicConfig(level=logging.INFO)
    #     logging.basicConfig(level=logging.DEBUG)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="basic.log" # optional! write logs to file, not console
    )

    logging.debug("debug msg")
    logging.info("info msg") 
    logging.warning ("warning msg")
    logging.error("error msg")
    logging.critical("critical msg")

if __name__ == "__main__":
    main()