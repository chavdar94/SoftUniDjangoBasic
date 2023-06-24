from plants_exam.plants.models import Profile


def get_profile(request):
    profile = Profile.objects.first()
    return {'profile': profile}
