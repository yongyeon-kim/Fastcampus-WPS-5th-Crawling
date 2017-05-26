class NaverWebtoon:
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        self.episode_list = []

    def get_info(self):
        return '정보 리턴'

    def view_last_episode(self):
        return ''

    def view_episode_list(self, num=1):
        return ''

    def save_webtoon(self, create_html=False):
        if create_html:
            return '다운받은 웹툰을 볼 수 있는 html까지 생성해서 저장'
        return '특정 경로에 웹툰 전체를 다운받아서 저장'