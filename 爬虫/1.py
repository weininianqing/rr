from urllib import request
if __name__ == '__main__':

    url="https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/video?lessonId=1052096226&courseId=1004987028"
    rsq = request.urlopen(url)

    html = rsq.read()
    html = html.decode("utf-8")

    print(html)