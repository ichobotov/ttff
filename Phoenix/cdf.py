import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go


knk_cmnv_30110 = [20.0, 21.0, 18.0, 22.0, 22.0, 23.0, 19.0, 18.0, 23.0, 22.0, 23.0, 21.0, 19.0, 22.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 123.0, 23.0, 23.0, 20.0, 19.0, 17.0, 19.0, 22.0, 27.0, 20.0, 20.0, 16.0, 21.0, 21.0, 20.0, 19.0, 18.0, 20.0, 20.0, 18.0, 18.0, 17.0, 18.0, 21.0, 22.0, 19.0, 19.0, 21.0, 18.0, 22.0, 22.0, 22.0, 20.0, 20.0, 19.0, 20.0, 19.0, 20.0, 20.0, 23.0, 22.0, 22.0, 20.0, 19.0, 20.0, 23.0, 18.0, 92.0, 24.0, 22.0, 19.0, 21.0, 19.0, 22.0, 22.0, 20.0, 24.0, 21.0, 22.0, 21.0, 27.0, 25.0, 20.0, 20.0, 22.0, 24.0, 29.0, 19.0, 20.0, 23.0, 22.0, 27.0, 22.0, 26.0, 22.0, 19.0, 26.0, 24.0, 91.0, 22.0, 23.0, 23.0, 24.0, 22.0, 22.0, 24.0, 25.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 346.0, 24.0, 22.0, 21.0, 28.0, 23.0, 19.0, 19.0, 20.0, 20.0, 21.0, 19.0, 17.0, 21.0, 18.0, 19.0, 19.0, 18.0, 19.0, 22.0, 21.0, 47.0, 19.0, 19.0, 18.0, 23.0, 20.0, 21.0, 24.0, 19.0, 22.0, 25.0, 38.0, 25.0, 24.0, 24.0, 22.0, 19.0, 21.0, 24.0, 19.0, 24.0, 24.0, 27.0, 33.0, 23.0, 20.0, 24.0, 24.0, 22.0, 20.0, 21.0, 20.0, 24.0, 23.0, 21.0, 20.0, 28.0, 26.0, 21.0, 22.0, 23.0, 20.0, 23.0, 25.0, 26.0, 23.0, 22.0, 20.0, 19.0, 22.0, 21.0, 24.0, 28.0, 28.0, 21.0, 25.0, 22.0, 22.0, 27.0, 25.0, 38.0, 48.0, 23.0, 23.0, 27.0, 32.0, 24.0, 23.0, 25.0, 22.0, 27.0, 23.0, 24.0, 24.0, 23.0, 23.0, 22.0, 25.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 292.0, 25.0, 24.0, 23.0, 22.0, 22.0, 21.0, 22.0, 20.0, 21.0, 21.0, 20.0, 27.0, 24.0, 18.0, 23.0, 24.0, 23.0, 23.0, 21.0, 24.0, 23.0, 23.0, 21.0, 23.0, 'fail', 23.0, 22.0, 80.0, 23.0, 24.0, 22.0, 31.0, 19.0, 23.0, 21.0, 28.0, 23.0, 24.0, 22.0, 21.0, 23.0, 23.0, 22.0, 21.0, 19.0, 22.0, 20.0, 21.0, 23.0, 24.0, 24.0, 22.0, 17.0, 22.0, 20.0, 92.0, 23.0, 'fail', 20.0, 20.0, 22.0, 19.0, 26.0, 17.0, 21.0, 32.0, 21.0, 23.0, 23.0, 22.0, 22.0, 25.0, 23.0, 23.0, 21.0, 26.0, 22.0, 27.0, 25.0, 24.0, 23.0, 21.0, 22.0, 20.0, 22.0, 26.0, 24.0, 26.0, 47.0, 25.0, 21.0, 21.0, 21.0, 23.0, 21.0, 25.0, 59.0, 198.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 137.0, 21.0, 24.0, 24.0, 20.0, 24.0, 23.0, 22.0, 24.0, 19.0, 22.0, 22.0, 20.0, 21.0, 18.0, 24.0, 21.0, 20.0, 18.0, 22.0, 24.0, 18.0, 23.0, 34.0, 21.0, 32.0, 28.0, 30.0, 31.0, 27.0, 20.0, 22.0, 22.0, 19.0, 23.0, 26.0, 21.0, 20.0, 22.0, 20.0, 23.0, 21.0, 19.0, 19.0, 21.0, 20.0, 21.0, 23.0, 21.0, 21.0, 20.0, 20.0, 22.0, 21.0, 21.0, 21.0, 24.0, 24.0, 24.0, 20.0, 21.0, 20.0, 19.0, 23.0, 31.0, 20.0, 20.0, 24.0, 24.0, 23.0, 21.0, 24.0, 23.0, 22.0, 22.0, 23.0, 22.0, 21.0, 24.0, 22.0, 22.0, 24.0, 23.0, 24.0, 22.0, 24.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 238.0, 24.0, 20.0, 25.0, 22.0, 19.0, 21.0, 24.0, 22.0, 21.0, 20.0, 19.0, 23.0, 24.0, 23.0, 21.0, 20.0, 20.0, 21.0, 22.0, 24.0, 19.0, 21.0, 18.0, 18.0, 21.0, 21.0, 37.0, 50.0, 263.0, 148.0]
knk_pho_30110 = [47.0, 48.0, 45.0, 52.0, 48.0, 47.0, 69.0, 52.0, 44.0, 61.0, 65.0, 63.0, 61.0, 63.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 362.0, 59.0, 60.0, 58.0, 59.0, 62.0, 57.0, 57.0, 84.0, 57.0, 81.0, 66.0, 57.0, 79.0, 49.0, 49.0, 47.0, 48.0, 45.0, 51.0, 43.0, 45.0, 70.0, 43.0, 64.0, 64.0, 66.0, 57.0, 55.0, 63.0, 62.0, 62.0, 64.0, 58.0, 59.0, 85.0, 57.0, 76.0, 62.0, 64.0, 83.0, 124.0, 55.0, 59.0, 77.0, 115.0, 53.0, 52.0, 53.0, 50.0, 50.0, 54.0, 50.0, 69.0, 72.0, 44.0, 71.0, 67.0, 65.0, 65.0, 89.0, 63.0, 61.0, 61.0, 93.0, 59.0, 57.0, 56.0, 174.0, 55.0, 78.0, 54.0, 76.0, 54.0, 58.0, 49.0, 141.0, 56.0, 45.0, 47.0, 73.0, 80.0, 70.0, 90.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 45.0, 47.0, 76.0, 69.0, 88.0, 88.0, 81.0, 65.0, 64.0, 62.0, 62.0, 61.0, 84.0, 62.0, 77.0, 57.0, 56.0, 56.0, 66.0, 82.0, 209.0, 51.0, 50.0, 66.0, 57.0, 56.0, 65.0, 54.0, 50.0, 52.0, 51.0, 90.0, 70.0, 68.0, 70.0, 66.0, 86.0, 65.0, 68.0, 84.0, 78.0, 80.0, 75.0, 60.0, 78.0, 67.0, 57.0, 55.0, 55.0, 100.0, 79.0, 'fail', 58.0, 49.0, 48.0, 47.0, 46.0, 58.0, 48.0, 47.0, 45.0, 41.0, 73.0, 64.0, 67.0, 62.0, 63.0, 64.0, 64.0, 61.0, 60.0, 165.0, 89.0, 93.0, 78.0, 87.0, 65.0, 85.0, 83.0, 86.0, 251.0, 81.0, 'fail', 57.0, 57.0, 55.0, 54.0, 52.0, 53.0, 48.0, 51.0, 40.0, 45.0, 46.0, 94.0, 86.0, 62.0, 158.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 383.0, 48.0, 54.0, 58.0, 54.0, 52.0, 42.0, 42.0, 69.0, 82.0, 71.0, 63.0, 65.0, 64.0, 63.0, 64.0, 64.0, 64.0, 61.0, 84.0, 70.0, 82.0, 59.0, 80.0, 55.0, 82.0, 81.0, 63.0, 144.0, 52.0, 61.0, 108.0, 64.0, 51.0, 74.0, 72.0, 71.0, 84.0, 69.0, 88.0, 83.0, 94.0, 95.0, 170.0, 154.0, 62.0, 63.0, 60.0, 93.0, 58.0, 'fail', 58.0, 69.0, 55.0, 58.0, 54.0, 111.0, 58.0, 50.0, 48.0, 47.0, 47.0, 45.0, 44.0, 66.0, 87.0, 74.0, 73.0, 60.0, 81.0, 70.0, 69.0, 55.0, 97.0, 96.0, 89.0, 94.0, 89.0, 87.0, 79.0, 63.0, 60.0, 84.0, 87.0, 80.0, 85.0, 84.0, 64.0, 83.0, 51.0, 50.0, 46.0, 61.0, 77.0, 57.0, 42.0, 42.0, 77.0, 98.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 381.0, 51.0, 57.0, 77.0, 58.0, 70.0, 53.0, 47.0, 67.0, 60.0, 'fail', 59.0, 58.0, 148.0, 58.0, 58.0, 68.0, 72.0, 78.0, 71.0, 69.0, 58.0, 172.0, 73.0, 101.0, 60.0, 70.0, 51.0, 69.0, 57.0, 55.0, 54.0, 54.0, 51.0, 55.0, 50.0, 63.0, 48.0, 63.0, 62.0, 56.0, 55.0, 58.0, 64.0, 64.0, 51.0, 51.0, 51.0, 49.0, 61.0, 46.0, 137.0, 74.0, 53.0, 52.0, 67.0, 50.0, 68.0, 69.0, 68.0, 66.0, 65.0, 53.0, 52.0, 53.0, 50.0, 43.0, 61.0, 60.0, 64.0, 58.0, 55.0, 58.0, 57.0, 63.0, 64.0, 61.0, 62.0, 59.0, 60.0, 'fail', 149.0, 63.0, 53.0, 214.0, 61.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 364.0, 195.0, 59.0, 78.0, 58.0, 157.0, 75.0, 60.0, 56.0, 52.0, 60.0, 53.0, 53.0, 52.0, 52.0, 52.0, 71.0, 55.0, 53.0, 62.0, 48.0, 60.0, 48.0, 198.0, 192.0, 67.0, 59.0, 67.0, 59.0, 76.0, 69.0]
knk_cmnv_30112 = [33.0, 33.0, 34.0, 33.0, 32.0, 120.0, 33.0, 34.0, 33.0, 32.0, 33.0, 32.0, 33.0, 32.0, 33.0, 37.0, 33.0, 34.0, 35.0, 33.0, 33.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 34.0, 34.0, 80.0, 33.0, 34.0, 33.0, 34.0, 33.0, 105.0, 61.0, 34.0, 33.0, 34.0, 34.0, 35.0, 33.0, 34.0, 33.0, 34.0, 46.0, 35.0, 34.0, 85.0, 34.0, 52.0, 35.0, 34.0, 34.0, 49.0, 58.0, 33.0, 33.0, 35.0, 35.0, 35.0, 34.0, 34.0, 34.0, 91.0, 33.0, 33.0, 34.0, 34.0, 40.0, 34.0, 33.0, 33.0, 34.0, 35.0, 244.0, 394.0, 33.0, 34.0, 33.0, 'fail', 'fail', 34.0, 35.0, 33.0, 234.0, 383.0, 33.0, 33.0, 34.0, 34.0, 32.0, 34.0, 34.0, 32.0, 58.0, 161.0, 'fail', 'fail', 'fail', 'fail', 32.0, 76.0, 34.0, 34.0, 214.0, 33.0, 34.0, 33.0, 60.0, 33.0, 34.0, 33.0, 33.0, 33.0, 35.0, 33.0, 33.0, 34.0, 35.0, 34.0, 33.0, 34.0, 34.0, 33.0, 34.0, 34.0, 34.0, 34.0, 35.0, 34.0, 34.0, 34.0, 35.0, 35.0, 36.0, 104.0, 34.0, 34.0, 36.0, 35.0, 35.0, 35.0, 34.0, 34.0, 84.0, 34.0, 34.0, 33.0, 35.0, 35.0, 33.0, 36.0, 33.0, 34.0, 34.0, 34.0, 34.0, 33.0, 34.0, 34.0, 34.0, 34.0, 34.0, 35.0, 36.0, 34.0, 35.0, 33.0, 34.0, 33.0, 34.0, 33.0, 35.0, 33.0, 33.0, 34.0, 34.0, 34.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 118.0, 33.0, 34.0, 33.0, 33.0, 269.0, 34.0, 'fail', 34.0, 33.0, 33.0, 34.0, 32.0, 33.0, 33.0, 39.0, 33.0, 33.0, 33.0, 34.0, 34.0, 33.0, 33.0, 33.0, 33.0, 34.0, 34.0, 34.0, 33.0, 33.0, 34.0, 33.0, 77.0, 33.0, 32.0, 33.0, 85.0, 33.0, 33.0, 33.0, 34.0, 33.0, 34.0, 33.0, 33.0, 34.0, 35.0, 35.0, 34.0, 34.0, 34.0, 75.0, 34.0, 'fail', 32.0, 33.0, 33.0, 34.0, 34.0, 34.0, 35.0, 293.0, 256.0, 35.0, 34.0, 34.0, 33.0, 34.0, 34.0, 34.0, 147.0, 34.0, 35.0, 35.0, 33.0, 33.0, 200.0, 35.0, 86.0, 33.0, 35.0, 33.0, 33.0, 34.0, 35.0, 34.0, 35.0, 34.0, 35.0, 35.0, 36.0, 106.0, 35.0, 35.0, 34.0, 35.0, 34.0, 35.0, 33.0, 34.0, 34.0, 72.0, 102.0, 35.0, 33.0, 33.0, 32.0, 35.0, 34.0, 34.0, 33.0, 35.0, 33.0, 33.0, 34.0, 78.0, 33.0, 33.0, 35.0, 34.0, 34.0, 32.0, 33.0, 44.0, 33.0, 103.0, 32.0, 35.0, 'fail', 32.0, 34.0, 33.0, 33.0, 33.0, 34.0, 32.0, 34.0, 115.0, 33.0, 32.0, 34.0, 44.0, 190.0, 34.0, 34.0, 34.0, 33.0, 33.0, 33.0, 59.0, 33.0, 34.0, 46.0, 35.0]
knk_pho_30112 = ['fail', 'fail', 53.0, 57.0, 54.0, 146.0, 55.0, 55.0, 53.0, 52.0, 52.0, 52.0, 51.0, 53.0, 50.0, 48.0, 46.0, 46.0, 132.0, 47.0, 43.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 79.0, 109.0, 51.0, 53.0, 49.0, 49.0, 47.0, 146.0, 76.0, 44.0, 50.0, 43.0, 124.0, 123.0, 39.0, 38.0, 37.0, 56.0, 65.0, 62.0, 147.0, 113.0, 59.0, 81.0, 58.0, 48.0, 48.0, 56.0, 85.0, 53.0, 53.0, 54.0, 53.0, 54.0, 47.0, 52.0, 47.0, 112.0, 50.0, 44.0, 'fail', 48.0, 40.0, 47.0, 41.0, 37.0, 47.0, 39.0, 40.0, 59.0, 82.0, 82.0, 'fail', 'fail', 'fail', 316.0, 107.0, 106.0, 54.0, 73.0, 102.0, 54.0, 51.0, 59.0, 48.0, 55.0, 46.0, 48.0, 44.0, 44.0, 'fail', 'fail', 'fail', 'fail', 71.0, 97.0, 37.0, 58.0, 54.0, 54.0, 55.0, 127.0, 57.0, 53.0, 61.0, 54.0, 101.0, 54.0, 55.0, 92.0, 55.0, 51.0, 78.0, 50.0, 68.0, 47.0, 47.0, 45.0, 44.0, 53.0, 75.0, 75.0, 104.0, 'fail', 108.0, 72.0, 75.0, 58.0, 35.0, 132.0, 67.0, 65.0, 65.0, 'fail', 62.0, 58.0, 60.0, 'fail', 214.0, 68.0, 53.0, 168.0, 66.0, 'fail', 48.0, 51.0, 46.0, 49.0, 47.0, 46.0, 92.0, 80.0, 205.0, 75.0, 44.0, 46.0, 40.0, 60.0, 55.0, 55.0, 55.0, 53.0, 54.0, 53.0, 55.0, 52.0, 56.0, 58.0, 55.0, 52.0, 51.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 126.0, 42.0, 44.0, 42.0, 38.0, 40.0, 59.0, 54.0, 57.0, 61.0, 53.0, 54.0, 52.0, 54.0, 55.0, 53.0, 53.0, 52.0, 50.0, 51.0, 50.0, 48.0, 56.0, 55.0, 44.0, 54.0, 52.0, 43.0, 41.0, 60.0, 43.0, 41.0, 58.0, 45.0, 48.0, 87.0, 55.0, 57.0, 62.0, 54.0, 91.0, 59.0, 49.0, 53.0, 46.0, 55.0, 74.0, 53.0, 55.0, 50.0, 48.0, 49.0, 50.0, 47.0, 54.0, 54.0, 43.0, 55.0, 51.0, 43.0, 49.0, 64.0, 57.0, 175.0, 72.0, 59.0, 53.0, 66.0, 56.0, 54.0, 60.0, 61.0, 61.0, 55.0, 53.0, 54.0, 53.0, 53.0, 110.0, 50.0, 49.0, 51.0, 46.0, 82.0, 67.0, 65.0, 65.0, 93.0, 63.0, 45.0, 44.0, 149.0, 69.0, 57.0, 69.0, 57.0, 77.0, 61.0, 161.0, 56.0, 62.0, 87.0, 125.0, 58.0, 63.0, 62.0, 52.0, 61.0, 51.0, 50.0, 48.0, 48.0, 'fail', 48.0, 53.0, 106.0, 45.0, 45.0, 41.0, 40.0, 46.0, 44.0, 56.0, 85.0, 54.0, 130.0, 54.0, 56.0, 111.0, 53.0, 54.0, 47.0, 56.0, 'fail', 55.0, 53.0, 53.0, 141.0, 50.0, 49.0, 48.0, 167.0, 45.0, 60.0, 45.0, 46.0, 45.0, 91.0, 41.0, 90.0, 56.0, 51.0, 58.0, 55.0]

pho_all_gnss_30110 = [65.0, 45.0, 44.0, 42.0, 61.0, 40.0, 39.0, 82.0, 57.0, 45.0, 34.0, 34.0, 33.0, 64.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 369.0, 41.0, 77.0, 64.0, 38.0, 238.0, 92.0, 207.0, 72.0, 32.0, 46.0, 53.0, 52.0, 101.0, 220.0, 51.0, 52.0, 38.0, 36.0, 35.0, 34.0, 33.0, 32.0, 56.0, 44.0, 61.0, 113.0, 46.0, 58.0, 38.0, 60.0, 47.0, 42.0, 70.0, 53.0, 80.0, 46.0, 26.0, 26.0, 393.0, 46.0, 85.0, 50.0, 51.0, 55.0, 66.0, 57.0, 312.0, 46.0, 106.0, 74.0, 63.0, 42.0, 71.0, 41.0, 40.0, 142.0, 97.0, 37.0, 36.0, 35.0, 33.0, 32.0, 51.0, 150.0, 29.0, 28.0, 28.0, 26.0, 24.0, 25.0, 43.0, 67.0, 42.0, 100.0, 43.0, 62.0, 43.0, 60.0, 46.0, 68.0, 69.0, 66.0, 69.0, 54.0, 66.0, 88.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 552.0, 72.0, 165.0, 136.0, 67.0, 172.0, 35.0, 35.0, 60.0, 34.0, 41.0, 43.0, 57.0, 57.0, 49.0, 26.0, 26.0, 26.0, 25.0, 24.0, 42.0, 60.0, 45.0, 43.0, 44.0, 68.0, 91.0, 66.0, 49.0, 73.0, 72.0, 72.0, 84.0, 70.0, 60.0, 67.0, 71.0, 69.0, 90.0, 123.0, 276.0, 59.0, 119.0, 138.0, 60.0, 61.0, 60.0, 54.0, 202.0, 58.0, 57.0, 55.0, 164.0, 57.0, 48.0, 47.0, 47.0, 42.0, 45.0, 43.0, 42.0, 41.0, 41.0, 38.0, 37.0, 36.0, 35.0, 34.0, 34.0, 33.0, 31.0, 31.0, 45.0, 68.0, 59.0, 65.0, 76.0, 85.0, 110.0, 207.0, 52.0, 'fail', 447.0, 228.0, 81.0, 206.0, 149.0, 118.0, 341.0, 342.0, 74.0, 212.0, 39.0, 38.0, 39.0, 193.0, 69.0, 96.0, 67.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 498.0, 42.0, 50.0, 66.0, 70.0, 73.0, 61.0, 40.0, 39.0, 127.0, 37.0, 48.0, 36.0, 66.0, 155.0, 32.0, 108.0, 190.0, 49.0, 61.0, 47.0, 58.0, 55.0, 57.0, 53.0, 68.0, 217.0, 320.0, 417.0, 82.0, 188.0, 181.0, 144.0, 94.0, 69.0, 65.0, 139.0, 69.0, 137.0, 105.0, 144.0, 216.0, 123.0, 153.0, 101.0, 31.0, 216.0, 38.0, 46.0, 28.0, 26.0, 25.0, 62.0, 81.0, 52.0, 20.0, 19.0, 172.0, 42.0, 105.0, 43.0, 60.0, 53.0, 94.0, 51.0, 73.0, 179.0, 63.0, 104.0, 89.0, 66.0, 102.0, 94.0, 161.0, 160.0, 65.0, 75.0, 118.0, 193.0, 59.0, 115.0, 114.0, 238.0, 172.0, 130.0, 42.0, 128.0, 51.0, 74.0, 50.0, 72.0, 46.0, 48.0, 45.0, 43.0, 44.0, 41.0, 39.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 316.0, 71.0, 202.0, 177.0, 57.0, 103.0, 71.0, 77.0, 458.0, 275.0, 305.0, 95.0, 34.0, 59.0, 60.0, 88.0, 140.0, 84.0, 327.0, 258.0, 198.0, 208.0, 75.0, 60.0, 159.0, 81.0, 138.0, 79.0, 67.0, 90.0, 65.0, 52.0, 65.0, 73.0, 63.0, 41.0, 70.0, 60.0, 39.0, 37.0, 35.0, 39.0, 34.0, 33.0, 31.0, 30.0, 29.0, 27.0, 48.0, 66.0, 58.0, 56.0, 53.0, 69.0, 48.0, 55.0, 62.0, 52.0, 202.0, 180.0, 59.0, 78.0, 69.0, 91.0, 91.0, 189.0, 53.0, 65.0, 41.0, 425.0, 50.0, 60.0, 35.0, 33.0, 50.0, 56.0, 28.0, 55.0, 66.0, 25.0, 55.0, 50.0, 74.0, 49.0, 43.0, 46.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 420.0, 43.0, 147.0, 57.0, 144.0, 115.0, 89.0, 87.0, 58.0, 56.0, 59.0, 49.0, 121.0, 60.0, 46.0, 66.0, 48.0, 75.0, 69.0, 205.0, 249.0, 67.0, 55.0, 66.0, 58.0, 68.0, 63.0, 33.0, 32.0, 85.0, 283.0]
pho_all_gnss_30112 = [51.0, 60.0, 29.0, 57.0, 27.0, 122.0, 63.0, 24.0, 46.0, 56.0, 42.0, 65.0, 44.0, 52.0, 51.0, 45.0, 43.0, 48.0, 48.0, 56.0, 42.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 316.0, 46.0, 43.0, 132.0, 43.0, 46.0, 47.0, 44.0, 44.0, 142.0, 74.0, 75.0, 41.0, 40.0, 39.0, 39.0, 37.0, 39.0, 39.0, 58.0, 451.0, 153.0, 95.0, 154.0, 59.0, 105.0, 57.0, 76.0, 55.0, 76.0, 113.0, 50.0, 58.0, 59.0, 80.0, 64.0, 75.0, 54.0, 49.0, 147.0, 66.0, 56.0, 44.0, 56.0, 59.0, 59.0, 41.0, 43.0, 35.0, 37.0, 66.0, 32.0, 60.0, 59.0, 92.0, 88.0, 72.0, 85.0, 293.0, 141.0, 81.0, 74.0, 104.0, 71.0, 49.0, 65.0, 46.0, 42.0, 44.0, 47.0, 46.0, 44.0, 'fail', 'fail', 'fail', 'fail', 50.0, 122.0, 49.0, 55.0, 47.0, 32.0, 80.0, 51.0, 56.0, 66.0, 40.0, 76.0, 53.0, 58.0, 52.0, 50.0, 49.0, 58.0, 61.0, 56.0, 53.0, 45.0, 44.0, 43.0, 43.0, 49.0, 57.0, 103.0, 68.0, 221.0, 182.0, 71.0, 70.0, 61.0, 31.0, 152.0, 61.0, 64.0, 63.0, 61.0, 60.0, 235.0, 174.0, 454.0, 'fail', 434.0, 204.0, 53.0, 44.0, 49.0, 194.0, 139.0, 50.0, 47.0, 140.0, 135.0, 41.0, 81.0, 66.0, 37.0, 36.0, 35.0, 34.0, 33.0, 33.0, 31.0, 60.0, 29.0, 28.0, 43.0, 55.0, 51.0, 25.0, 22.0, 71.0, 173.0, 84.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 553.0, 141.0, 67.0, 70.0, 122.0, 61.0, 64.0, 51.0, 64.0, 49.0, 58.0, 57.0, 61.0, 60.0, 55.0, 53.0, 45.0, 49.0, 42.0, 46.0, 47.0, 52.0, 54.0, 43.0, 49.0, 73.0, 47.0, 47.0, 40.0, 56.0, 42.0, 42.0, 55.0, 44.0, 108.0, 49.0, 32.0, 55.0, 30.0, 53.0, 51.0, 65.0, 40.0, 60.0, 24.0, 23.0, 46.0, 21.0, 46.0, 57.0, 68.0, 56.0, 42.0, 43.0, 44.0, 72.0, 88.0, 69.0, 72.0, 70.0, 97.0, 67.0, 69.0, 51.0, 75.0, 56.0, 64.0, 360.0, 62.0, 56.0, 60.0, 83.0, 387.0, 323.0, 59.0, 67.0, 51.0, 45.0, 42.0, 140.0, 52.0, 51.0, 50.0, 195.0, 436.0, 106.0, 132.0, 135.0, 63.0, 99.0, 69.0, 52.0, 125.0, 160.0, 33.0, 60.0, 93.0, 209.0, 59.0, 62.0, 451.0, 'fail', 179.0, 'fail', 177.0, 41.0, 163.0, 54.0, 41.0, 79.0, 44.0, 43.0, 45.0, 'fail', 43.0, 42.0, 131.0, 160.0, 242.0, 39.0, 58.0, 68.0, 52.0, 64.0, 135.0, 61.0, 156.0, 180.0, 46.0, 148.0, 50.0, 70.0, 46.0, 47.0, 43.0, 23.0, 22.0, 43.0, 167.0, 62.0, 43.0, 47.0, 254.0, 43.0, 42.0, 57.0, 68.0, 54.0, 40.0, 39.0, 120.0, 40.0, 62.0, 343.0, 60.0, 66.0]
pho_all_gnss_30112v2 = [52.0, 60.0, 30.0, 58.0, 28.0, 122.0, 64.0, 25.0, 46.0, 57.0, 42.0, 65.0, 44.0, 53.0, 52.0, 46.0, 44.0, 49.0, 48.0, 57.0, 43.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 47.0, 44.0, 133.0, 44.0, 47.0, 48.0, 45.0, 45.0, 143.0, 75.0, 76.0, 42.0, 41.0, 40.0, 39.0, 38.0, 40.0, 40.0, 59.0, 452.0, 153.0, 96.0, 155.0, 60.0, 106.0, 58.0, 77.0, 56.0, 76.0, 113.0, 50.0, 59.0, 59.0, 80.0, 63.0, 76.0, 54.0, 49.0, 148.0, 66.0, 57.0, 45.0, 56.0, 60.0, 59.0, 41.0, 44.0, 35.0, 38.0, 67.0, 32.0, 61.0, 60.0, 93.0, 89.0, 73.0, 85.0, 294.0, 142.0, 82.0, 75.0, 104.0, 71.0, 49.0, 66.0, 47.0, 42.0, 45.0, 48.0, 47.0, 45.0, 'fail', 'fail', 'fail', 'fail', 51.0, 122.0, 49.0, 56.0, 47.0, 32.0, 81.0, 52.0, 57.0, 66.0, 41.0, 77.0, 54.0, 58.0, 52.0, 51.0, 50.0, 58.0, 62.0, 56.0, 53.0, 46.0, 45.0, 44.0, 43.0, 49.0, 57.0, 104.0, 69.0, 222.0, 183.0, 72.0, 71.0, 62.0, 32.0, 153.0, 61.0, 64.0, 63.0, 62.0, 61.0, 236.0, 175.0, 455.0, 497.0, 435.0, 205.0, 54.0, 45.0, 49.0, 195.0, 140.0, 51.0, 48.0, 141.0, 136.0, 41.0, 82.0, 67.0, 38.0, 37.0, 36.0, 34.0, 34.0, 33.0, 32.0, 60.0, 29.0, 28.0, 44.0, 55.0, 52.0, 24.0, 23.0, 72.0, 173.0, 85.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 85.0, 142.0, 67.0, 70.0, 123.0, 62.0, 65.0, 52.0, 64.0, 50.0, 59.0, 58.0, 61.0, 60.0, 55.0, 54.0, 46.0, 50.0, 43.0, 46.0, 47.0, 52.0, 55.0, 44.0, 49.0, 73.0, 47.0, 47.0, 41.0, 56.0, 43.0, 42.0, 55.0, 44.0, 109.0, 50.0, 33.0, 55.0, 31.0, 54.0, 51.0, 66.0, 41.0, 60.0, 24.0, 24.0, 47.0, 22.0, 46.0, 58.0, 69.0, 56.0, 43.0, 44.0, 45.0, 72.0, 89.0, 70.0, 73.0, 71.0, 98.0, 68.0, 69.0, 52.0, 75.0, 57.0, 65.0, 361.0, 63.0, 57.0, 61.0, 84.0, 388.0, 324.0, 59.0, 68.0, 51.0, 46.0, 43.0, 141.0, 53.0, 52.0, 51.0, 196.0, 437.0, 106.0, 133.0, 136.0, 64.0, 100.0, 69.0, 54.0, 125.0, 161.0, 34.0, 62.0, 93.0, 209.0, 58.0, 63.0, 'fail', 'fail', 180.0, 'fail', 'fail', 42.0, 164.0, 55.0, 42.0, 80.0, 44.0, 44.0, 46.0, 'fail', 'fail', 43.0, 132.0, 161.0, 243.0, 39.0, 58.0, 69.0, 53.0, 64.0, 136.0, 62.0, 156.0, 181.0, 47.0, 148.0, 51.0, 71.0, 46.0, 47.0, 44.0, 23.0, 22.0, 43.0, 168.0, 63.0, 44.0, 47.0, 255.0, 44.0, 42.0, 57.0, 68.0, 55.0, 41.0, 39.0, 120.0, 41.0, 62.0, 344.0, 60.0, 67.0]
pho_glo_irn_off = [396.0, 473.0, 231.0, 184.0, 341.0, 'fail', 257.0, 284.0, 'fail', 216.0, 370.0, 201.0, 124.0, 195.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 490.0, 273.0, 218.0, 475.0, 'fail', 'fail', 'fail', 273.0, 'fail', 330.0, 239.0, 584.0, 382.0, 245.0, 'fail', 222.0, 258.0, 38.0, 37.0, 37.0, 35.0, 34.0, 44.0, 166.0, 161.0, 314.0, 136.0, 194.0, 56.0, 52.0, 176.0, 130.0, 55.0, 330.0, 270.0, 398.0, 364.0, 482.0, 425.0, 392.0, 242.0, 'fail', 478.0, 224.0, 290.0, 264.0, 534.0, 'fail', 352.0, 471.0, 320.0, 498.0, 378.0, 131.0, 139.0, 180.0, 258.0, 222.0, 221.0, 220.0, 339.0, 201.0, 'fail', 437.0, 399.0, 'fail', 299.0, 'fail', 364.0, 'fail', 315.0, 'fail', 262.0, 'fail', 447.0, 198.0, 459.0, 347.0, 'fail', 405.0, 382.0, 454.0, 'fail', 132.0, 370.0, 180.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 410.0, 263.0, 'fail', 286.0, 546.0, 233.0, 221.0, 520.0, 370.0, 196.0, 216.0, 95.0, 59.0, 63.0, 62.0, 74.0, 84.0, 59.0, 58.0, 87.0, 'fail', 351.0, 393.0, 189.0, 394.0, 442.0, 320.0, 'fail', 'fail', 'fail', 406.0, 431.0, 150.0, 338.0, 171.0, 191.0, 163.0, 514.0, 93.0, 407.0, 277.0, 429.0, 208.0, 346.0, 'fail', 377.0, 313.0, 294.0, 'fail', 268.0, 368.0, 291.0, 190.0, 443.0, 189.0, 175.0, 405.0, 254.0, 'fail', 'fail', 432.0, 495.0, 374.0, 406.0, 342.0, 461.0, 'fail', 357.0, 98.0, 323.0, 196.0, 432.0, 'fail', 495.0, 483.0, 'fail', 'fail', 453.0, 532.0, 506.0, 'fail', 'fail', 'fail', 473.0, 'fail', 'fail', 350.0, 'fail', 229.0, 476.0, 'fail', 295.0, 308.0, 462.0, 371.0, 215.0, 490.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 566.0, 321.0, 240.0, 434.0, 232.0, 587.0, 196.0, 345.0, 374.0, 343.0, 178.0, 221.0, 276.0, 339.0, 213.0, 97.0, 271.0, 185.0, 215.0, 243.0, 318.0, 'fail', 90.0, 329.0, 329.0, 207.0, 200.0, 381.0, 'fail', 533.0, 309.0, 534.0, 174.0, 284.0, 403.0, 266.0, 95.0, 225.0, 243.0, 428.0, 277.0, 276.0, 124.0, 445.0, 'fail', 'fail', 336.0, 271.0, 94.0, 181.0, 212.0, 422.0, 61.0, 212.0, 201.0, 129.0, 465.0, 288.0, 317.0, 221.0, 187.0, 202.0, 259.0, 178.0, 185.0, 180.0, 172.0, 181.0, 480.0, 448.0, 177.0, 176.0, 325.0, 486.0, 307.0, 187.0, 248.0, 202.0, 195.0, 297.0, 135.0, 265.0, 300.0, 328.0, 207.0, 462.0, 260.0, 170.0, 108.0, 334.0, 294.0, 'fail', 366.0, 182.0, 183.0, 221.0, 225.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 259.0, 293.0, 318.0, 472.0, 316.0, 'fail', 344.0, 472.0, 'fail', 268.0, 220.0, 'fail', 587.0, 468.0, 395.0, 441.0, 363.0, 242.0, 296.0, 600.0, 569.0, 508.0, 283.0, 460.0, 595.0, 444.0, 294.0, 137.0, 136.0, 321.0, 134.0, 229.0, 132.0, 302.0, 105.0, 138.0, 266.0, 102.0, 246.0, 150.0, 162.0, 139.0, 122.0, 78.0, 220.0, 65.0, 124.0, 182.0, 124.0, 90.0, 195.0, 143.0, 185.0, 267.0, 324.0, 62.0, 191.0, 471.0, 232.0, 352.0, 442.0, 390.0, 508.0, 467.0, 315.0, 418.0, 473.0, 174.0, 411.0, 490.0, 445.0, 338.0, 280.0, 'fail', 'fail', 498.0, 333.0, 456.0, 189.0, 466.0, 211.0, 209.0, 373.0, 461.0, 205.0, 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 'fail', 133.0, 177.0, 182.0, 147.0, 146.0, 114.0, 388.0, 190.0, 270.0, 517.0, 114.0, 267.0, 158.0, 121.0, 110.0, 134.0, 184.0, 184.0, 409.0, 479.0, 249.0, 313.0, 'fail', 284.0, 485.0, 190.0, 'fail', 535.0, 489.0, 337.0]
pho_barnayl_cold_starts = [32.0, 33.0, 35.0, 42.0, 29.0, 28.0, 26.0, 26.0, 25.0, 24.0, 23.0, 22.0, 41.0, 40.0, 41.0, 38.0, 39.0, 40.0, 41.0, 40.0, 39.0, 38.0, 38.0, 36.0, 36.0, 34.0, 40.0, 32.0, 182.0, 33.0, 70.0, 29.0, 28.0, 38.0, 26.0, 25.0, 24.0, 29.0, 540.0, 583.0, 40.0, 20.0, 40.0, 39.0, 39.0, 42.0, 42.0, 39.0, 41.0, 37.0, 37.0, 94.0, 35.0, 31.0, 30.0, 29.0, 24.0, 24.0, 30.0, 22.0, 43.0, 41.0, 44.0, 43.0, 44.0, 42.0, 41.0, 41.0, 41.0, 36.0, 35.0, 34.0, 33.0, 263.0, 28.0, 27.0, 38.0, 255.0, 24.0, 45.0, 44.0, 47.0, 42.0, 45.0, 43.0, 43.0, 46.0, 44.0, 44.0, 43.0, 42.0, 41.0, 42.0, 39.0, 42.0, 37.0, 37.0, 35.0, 34.0, 33.0, 33.0, 31.0, 30.0, 275.0, 28.0, 27.0, 26.0, 26.0, 76.0, 43.0, 42.0, 41.0, 212.0, 39.0, 40.0, 40.0, 39.0, 41.0, 43.0, 40.0, 39.0, 38.0, 36.0]
pho_barnayl_reboot = [33.0, 32.0, 31.0, 31.0, 29.0, 28.0, 27.0, 26.0, 30.0, 27.0, 25.0, 26.0, 29.0, 31.0, 32.0, 31.0, 30.0, 30.0, 27.0, 31.0, 31.0, 31.0, 30.0, 30.0, 32.0, 29.0, 33.0, 32.0, 34.0, 30.0, 29.0, 32.0, 32.0, 30.0, 29.0, 28.0, 28.0, 26.0, 25.0, 28.0, 32.0, 30.0, 35.0, 37.0, 36.0, 35.0, 32.0, 34.0, 37.0, 31.0, 32.0, 31.0, 31.0, 30.0, 29.0, 28.0, 32.0, 37.0, 35.0, 34.0, 34.0, 33.0, 32.0, 30.0, 29.0, 28.0, 28.0, 27.0, 25.0, 26.0, 24.0, 30.0, 29.0, 28.0, 32.0, 31.0, 34.0, 33.0, 32.0, 32.0, 35.0, 29.0, 34.0, 29.0, 28.0, 31.0, 38.0, 35.0, 35.0, 34.0, 33.0, 33.0, 30.0, 29.0, 29.0, 33.0, 28.0, 28.0, 39.0, 33.0, 36.0, 33.0, 30.0, 31.0, 32.0, 31.0, 30.0, 29.0, 28.0, 31.0, 31.0, 31.0, 30.0, 29.0, 27.0, 27.0]
pho_barnayl_cold_starts_plus_linux = [45.68, 46.68, 48.68, 55.68, 42.68, 41.68, 39.68, 39.68, 38.68, 37.68, 36.68, 35.68, 54.68, 53.68, 54.68, 51.68, 52.68, 53.68, 54.68, 53.68, 52.68, 51.68, 51.68, 49.68, 49.68, 47.68, 53.68, 45.68, 46.68, 42.68, 41.68, 51.68, 39.68, 38.68, 37.68, 42.68, 53.68, 33.68, 53.68, 52.68, 52.68, 55.68, 55.68, 52.68, 54.68, 50.68, 50.68, 48.68, 44.68, 43.68, 42.68, 37.68, 37.68, 43.68, 35.68, 56.68, 54.68, 57.68, 56.68, 57.68, 55.68, 54.68, 54.68, 54.68, 49.68, 48.68, 47.68, 46.68, 41.68, 40.68, 51.68, 37.68, 58.68, 57.68, 60.68, 55.68, 58.68, 56.68, 56.68, 59.68, 57.68, 57.68, 56.68, 55.68, 54.68, 55.68, 52.68, 55.68, 50.68, 50.68, 48.68, 47.68, 46.68, 46.68, 44.68, 43.68, 41.68, 40.68, 39.68, 39.68, 56.68, 55.68, 54.68, 52.68, 53.68, 53.68, 52.68, 54.68, 56.68, 53.68, 52.68, 51.68, 49.68]
pho_barnayl_warm_starts = [39.0, 35.0, 46.0, 33.0, 44.0, 44.0, 41.0, 43.0, 34.0, 42.0, 41.0, 41.0, 38.0, 39.0, 37.0, 35.0, 34.0, 33.0, 32.0, 32.0, 31.0, 30.0, 29.0, 27.0, 26.0, 26.0, 24.0, 28.0, 23.0, 22.0, 38.0, 40.0, 43.0, 50.0, 46.0, 42.0, 46.0, 44.0, 41.0, 42.0, 40.0, 38.0, 39.0, 37.0, 37.0, 35.0, 36.0, 33.0, 32.0, 32.0, 30.0, 30.0, 28.0, 27.0, 27.0, 25.0, 24.0, 23.0, 22.0, 21.0, 20.0, 19.0, 41.0, 40.0, 38.0, 36.0, 40.0, 34.0, 33.0, 39.0, 39.0, 38.0, 37.0, 37.0, 37.0, 35.0, 35.0, 34.0, 38.0, 37.0, 39.0, 30.0, 29.0, 28.0, 43.0, 38.0, 45.0, 42.0, 43.0, 42.0, 41.0, 40.0, 38.0, 40.0, 39.0, 39.0, 37.0, 44.0, 41.0, 33.0, 39.0, 40.0, 39.0, 38.0, 37.0, 38.0, 35.0, 40.0, 34.0, 33.0, 38.0, 30.0, 30.0, 29.0, 27.0, 26.0, 25.0, 24.0, 23.0, 22.0, 21.0, 21.0, 40.0, 39.0, 38.0, 38.0, 36.0, 40.0, 42.0, 40.0, 38.0, 39.0, 40.0, 38.0, 38.0, 36.0, 36.0, 35.0, 37.0, 33.0, 40.0, 39.0, 38.0, 37.0]
pho_barnayl_warm_starts_plus_linux = [52.68, 48.68, 59.68, 46.68, 57.68, 57.68, 54.68, 56.68, 47.68, 55.68, 54.68, 54.68, 51.68, 52.68, 50.68, 48.68, 47.68, 46.68, 45.68, 45.68, 44.68, 43.68, 42.68, 40.68, 39.68, 39.68, 37.68, 41.68, 36.68, 35.68, 51.68, 53.68, 56.68, 63.68, 59.68, 55.68, 59.68, 57.68, 54.68, 55.68, 53.68, 51.68, 52.68, 50.68, 50.68, 48.68, 49.68, 46.68, 45.68, 45.68, 43.68, 43.68, 41.68, 40.68, 40.68, 38.68, 37.68, 36.68, 35.68, 34.68, 33.68, 32.68, 54.68, 53.68, 51.68, 49.68, 53.68, 47.68, 46.68, 52.68, 52.68, 51.68, 50.68, 50.68, 50.68, 48.68, 48.68, 47.68, 51.68, 50.68, 52.68, 43.68, 42.68, 41.68, 56.68, 51.68, 58.68, 55.68, 56.68, 55.68, 54.68, 53.68, 51.68, 53.68, 52.68, 52.68, 50.68, 57.68, 54.68, 46.68, 52.68, 53.68, 52.68, 51.68, 50.68, 51.68, 48.68, 53.68, 47.68, 46.68, 51.68, 43.68, 43.68, 42.68, 40.68, 39.68, 38.68, 37.68, 36.68, 35.68, 34.68, 34.68, 53.68, 52.68, 51.68, 51.68, 49.68, 53.68, 55.68, 53.68, 51.68, 52.68, 53.68, 51.68, 51.68, 49.68, 49.68, 48.68, 50.68, 46.68, 53.68, 52.68, 51.68, 50.68]

units={
    # 'knk_cmnv_30110': knk_cmnv_30110,
    # 'knk_pho_30110': knk_pho_30110,
    # 'knk_cmnv_30112': knk_cmnv_30112,
    # 'knk_pho_30112': knk_pho_30112,
    # 'Pho_3.0.110': pho_all_gnss_30110,
    'Pho_3.0.112': pho_all_gnss_30112,
    'pho_all_gnss_30112v2': pho_all_gnss_30112v2,
    # 'Pho_board_glo_irn_off': pho_glo_irn_off,
    # 'pho_barnayl_cold_starts':pho_barnayl_cold_starts,
    # 'pho_barnayl_cold_starts+start_linux':pho_barnayl_cold_starts_plus_linux,
    # 'pho_barnayl_reboot':pho_barnayl_reboot,
    # 'pho_barnayl_warm_starts': pho_barnayl_warm_starts,
    # 'pho_barnayl_warm_starts+start_linux': pho_barnayl_warm_starts_plus_linux
    }

data_for_plotly = []

plt.figure()
# plt.subplot(211)

for unit,trials in units.items():
    sucessful = [x for x in trials if x != 'fail']
    # sucessful = [x for x in trials if x != 'fail' and x < 70]
    # sort the data:
    data_sorted = np.sort(sucessful)
    # calculate the proportional values of samples
    p = 1. * np.arange(len(sucessful)) / (len(sucessful) - 1)
    plt.plot(data_sorted, p, label=f"{unit}", drawstyle='steps-post')
    data_for_plotly.append(go.Scatter(y=p, x=data_sorted, name=f"{unit}"))


# pho_barnayl = [x for x in pho_barnayl if x != 'fail' and x < 70]

plt.grid(True)
plt.xticks(np.arange(0, 600, 50))
# plt.xticks(np.arange(min(pho_barnayl), max(pho_barnayl), 2))
plt.legend()
# plt.legend(loc='upper left')
plt.savefig('ecdf.png')

# plt.figure()
# # plt.subplot(212)
# data = pho_barnayl_warm_starts
# plt.plot(data)
# # plt.plot([x for x in pho_barnayl_cold_starts if x < 70])
# plt.xticks(np.arange(0, len(data)+1, 10))
# plt.yticks(np.arange(int(min(data)), max(data)+1, 2))
# plt.grid(True)
# plt.ylabel('sec')
# plt.xlabel('trials')
# plt.savefig('graph.png')

#
# fig = go.Figure(data=data_for_plotly)
# fig.write_html("file.html")
# fig.show()


