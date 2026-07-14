def parse_release_marker(value: str) -> tuple[str,str]:
    channel,sep,version=value.strip().partition(":")
    if not sep or not channel or not version: raise ValueError("release marker must be channel:version")
    return channel,version
