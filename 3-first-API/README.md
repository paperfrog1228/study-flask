## 3.  첫 API 개발 시작

이론적인 내용은 별도로 저장해놨다.

플라스크 설치와 실제로 사용을 하였고,

ssh로 작업하고 있기에 외부에서 접속해보기 위해

```bash
FLASK_APP=app.py FLASK_DEBUG=1 flask run
```

대신

```bash
python {폴더 경로/app.py}
```

로 실행시켜서 외부 접속 허용시켰다. 왜 위에 것으로 하면 안되는지 아직은 모름.



추가적으로

```bash
source deactivate
```

이게 정말 안먹히는데

```bash
conda deactivate
```

는 잘먹힌다. 



그냥 콘다 설치하고 환경변수 export 하는데 진짜 시간을 많이 쓴 챕터이다.

httpie 써서 테스트 해봐라는데 더럽게 안먹혀서 갖다 버림.