from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="WORKSHOP",
    settings_files=["app/config/settings.yaml", "app/config/.secrets.yaml"],
    merge_enabled=True,
)
