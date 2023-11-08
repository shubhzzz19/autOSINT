from social_analyzer import SocialAnalyzer

def find_social_media_profiles(email):
    # Initialize the SocialAnalyzer instance
    sa = SocialAnalyzer()
    
    # Perform the analysis for the given email address
    analysis = sa.analyze_email(email)

    # Get social media profiles from the analysis
    social_profiles = analysis.get_social_profiles()

    if social_profiles:
        print(f'Social Media Profiles for {email}:')
        for profile in social_profiles:
            print(f"- {profile.platform}: {profile.url}")
    else:
        print(f'No social media profiles found for {email}')

if __name__ == "__main__":
    email_to_check = 'email@example.com'  # Replace with the email address you want to analyze
    find_social_media_profiles(email_to_check)
