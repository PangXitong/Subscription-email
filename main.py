from flask import Flask, request

app = Flask(__name__)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    print(email)

    # 将邮箱地址追加保存到文件中
    with open('./email.txt', 'a') as file:
        file.write(email + '\n')

    # 返回响应给客户端，表示订阅成功
    return '订阅成功！'

if __name__ == '__main__':
    app.run(port=1001)