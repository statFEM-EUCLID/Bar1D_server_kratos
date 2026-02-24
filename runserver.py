import umbridge
import src.KratosBar_Server

bar_model = src.KratosBar_Server.BarModel()
umbridge.serve_models([bar_model], 4242)
