import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 

def main(): 
	df = pd.read_csv('TACT.csv')
	st.title('Phân tích mức độ thuộc bài của học sinh')
	vk = pd.read_csv('TRONG.csv')
    	X = df['MEANING'].values.copy()
    	X1 = df['WORD'].values.copy()
  	X2 = kq['WORD'].values.copy()
    	CheckAccuracyTab, AnalyzeTab = st.tabs(['Học từ vựng và Kiểm tra','Phân tích thống kê'])

    	with CheckAccuracyTab:
        	st.header('ĐỀ')
		vk['MEANING']=X
		st.write(vk.heah(n=25))
		st.header('ĐÁP ÁN')
		st.write('Lưu ý: tạo file excel dòng đầu là WORD, các dòng tiếp theo là đáp án, không biết ghi null, đáp án viết thường, lưu file dạng .csv tải lên MyDrive với tên kq.csv')
		from google.colab import drive
		drive.mount('/content/drive')
		kq = pd.read_csv('/content/drive/MyDrive/kq.csv')
        
    	with AnalyzeTab:
        	st.header('Phân tích dữ liệu')
        	tab1, tab2 = st.tabs(["Kết quả","Phân tích, đánh giá"])
        	with tab1:
	    		dung = 0
	    		for i in range(25):
				if (X1[i]==X2[i]):
		     			dung += 1
	    		sai = 25 - dung
	    		st.print('Bạn có ',dung,' câu đúng!', end='')
	    		st.print('Bạn có ',sai,' câu sai!', end='')
	    		if (dung-sai<=5):
				st.print('Bạn đã đúng đa số các câu. Chúc mừng bạn!')
				st.balloons()
	    		else:
				st.print('Bạn đã sai khá nhiều từ. Bạn cần cố gắng hơn.')		
		
        	with tab2:
	    		A = []
	    		B = []
	    		for i in range(25):
				if (X1[i]==X2[i]):
		     			B.append(True)
				elif (X2[i]=='Null'):
		     			B.append(Null)	
				else:
		     			B.append(False)
            		for i in range(1,26):
  				A.append(i)
	    		kq['STT'] = A
	    		kq['TRUE/FALSE'] = B
	    		st.header('BIỂU ĐỒ TRÒN TỈ LỆ ĐÚNG SAI')
	    		px.pie(df, names="TRUE/FALSE")

if __name__ == '__main__':
	main()
