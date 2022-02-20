# 손글씨 숫자 인식기
화면에 숫자를 그리면 그 숫자가 무엇인지 인식하여 나타내는 웹사이트  
* [Link To Website](https://digit-prediction-seuha516.netlify.app)

## Example
<img src="https://user-images.githubusercontent.com/79067549/113823516-b537a980-97b9-11eb-8953-781943a00802.png" width="20%" height="20%">
<img src="https://user-images.githubusercontent.com/79067549/113823710-f0d27380-97b9-11eb-996d-0e180ba92c87.png" width="50%" height="50%">

*****
## BackEnd
* BackEnd: *Flask*
* 구현 기능:
  * 이미지 파일을 받아서 흑백 28*28픽셀로 변환
  * 미리 구현한 합성곱 신경망 모델에 입력
  * 출력값을 예측 답과 그 확률로 반환

## Other
* [DigitPrediction_FrontEnd](https://github.com/seuha516/digit-prediction-react-frontend)
* [Deeplearning Model (Colab)](https://github.com/seuha516/digit-prediction-flask-backend/blob/master/DigitPrediction.ipynb)
