from c_api import Api


repo = 'd:\\temp\\test\\'
k_api = '15c9a5c367msh4b3db71995ecbd2p11b32bjsn422839c9a3a4'
u_id = '6943972350728700930'

api = Api(repo=repo, key_api=k_api, user_id=u_id)
api.create_csv_video()
api.download_videos()
