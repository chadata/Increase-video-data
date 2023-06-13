# Increase-video-data

```
# 데이터 증대를 위한 이미지 처리 코드

이 저장소는 데이터 증대를 위한 이미지 처리 코드를 포함하고 있습니다. 이 코드는 OpenCV를 사용하여 이미지를 읽어와 다양한 변환을 적용한 후 결과를 저장합니다. 주어진 디렉토리의 이미지를 뒤집고 그레이스케일로 변환하는 등의 작업을 수행합니다.

## 사용 방법

1. 저장소를 클론합니다:

   ```shell
   git clone https://github.com/your-username/your-repository.git
   ```

2. Python 환경을 설정하고 필요한 패키지를 설치합니다:

   ```shell
   pip install opencv-python matplotlib
   ```

3. 코드를 실행하기 전에 `Hands` 디렉토리에 처리할 이미지 파일들을 준비합니다.

4. `main.py` 파일을 열고 `Hands` 디렉토리와 `Result` 디렉토리를 각각 올바른 경로로 수정합니다.

5. 코드를 실행하여 데이터 증대 작업을 수행합니다:

   ```shell
   python main.py
   ```

   이 코드는 `Hands` 디렉토리에 있는 이미지들을 읽어와 변환을 적용한 후 `Result` 디렉토리에 결과를 저장합니다.

6. 처리된 이미지들은 `Result` 디렉토리에 저장되어 있습니다.

## 참고 사항

- 코드는 Python 3 버전에서 작성되었습니다.
- 이미지 처리를 위해 OpenCV와 matplotlib 패키지가 필요합니다.
- 코드를 실행하기 전에 이미지 파일들이 포함된 `Hands` 디렉토리를 준비해야 합니다.
- 코드 실행 후 처리된 이미지들은 `Result` 디렉토리에 저장됩니다.
- 화면에 이미지를 표시하는 부분은 제거되었습니다.

```
