from django.utils import timezone


def get_elapsed_time(last_verified_at):
    now = timezone.now()
    difference = now - last_verified_at
    days = difference.days
    if days > 0:
        return f"{days}d ago"
    hours, remainder = divmod(difference.seconds, 3600)
    if hours > 0:
        return f"{hours}h ago"
    minutes, seconds = divmod(remainder, 60)
    if minutes > 0:
        return f"{minutes}m ago"
    return "Less than a minute ago"
