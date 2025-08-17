from config import settings

def fetch_configuration_details():
    """
    Fetch site configuration details from settings.SITE.

    Returns:
        list of dict: Each dict contains site URL, max_attempts, and back_off.
    """
    try:
        site_configs = settings.SITE
        if not isinstance(site_configs, list):
            raise ValueError("SITE in settings.py must be a list of site configurations")
        return site_configs
    except AttributeError:
        raise AttributeError("settings.py does not define 'SITE'")
    except Exception as e:
        print(f"[ERROR] Failed to fetch configuration details: {e}")
        return []
