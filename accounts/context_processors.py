def user_social_links(request):
    if request.user.is_authenticated:
        return {
            'github' : request.user.github,
            'linkedin' : request.user.linkedin,
        }
    return {}