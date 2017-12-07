import falcon


class MainResource:
    def on_post(self, req, resp):
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote


api = falcon.API()
api.add_route('/', MainResource())
