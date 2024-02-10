from yaml import safe_load

CONFIG_PATH = "config.yaml"


def get_settings(config_name: str=CONFIG_PATH):
    with open(config_name, 'r') as f:
        data = safe_load(f)

    return data


def get_db_url(config_name: str=CONFIG_PATH):
    settings = get_settings(config_name)
    
    return f"postgresql://{settings['databases']['bonus_db']['user']}:"\
                        f"{settings['databases']['bonus_db']['password']}@"\
                        f"{settings['databases']['bonus_db']['host']}:"\
                        f"{settings['databases']['bonus_db']['port']}/"\
                        f"{settings['databases']['bonus_db']['db']}"
