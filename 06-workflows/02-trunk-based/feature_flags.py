FEATURE_FLAGS = {
    "new_metrics_endpoint": False,
    "enhanced_logging": True,
    "dark_mode": False,
    "new_dashboard": False,
}


def is_enabled(flag_name: str) -> bool:
    """Check if a feature flag is enabled."""
    return FEATURE_FLAGS.get(flag_name, False)
