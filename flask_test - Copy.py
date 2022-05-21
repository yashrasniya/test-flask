from flask import Flask,render_template,make_response
import pdfkit
app = Flask(__name__)
@app.route("/")
def home():
	return render_template("mail.html")
@app.route("/pdf/<student_name>/<sem>/<year>/<roll_number>/<fname>/<assignmentTitle>/<subName>")
def pdf(student_name,sem,year,roll_number,fname,assignmentTitle,subName):
	
	ren=render_template("js.html",student_name=student_name,sem=sem,year=year,roll_number=roll_number,fname=fname,
		assignmentTitle=assignmentTitle,subName=subName)
	print(ren)
	options = {
		'page-size': 'Letter',
		'margin-top': '0.75in',
		'margin-right': '0.75in',
		'margin-bottom': '0.75in',
		'margin-left': '0.75in',
		'encoding': "UTF-8",
		'custom-header': [
			('Accept-Encoding', 'gzip')
		],
		'cookie': [
			('cookie-empty-value', '""'),
			('cookie-name1', 'cookie-value1'),
			('cookie-name2', 'cookie-value2'),
		],
		'no-outline': None
	}
	pdf=pdfkit.from_string(ren,options=options)
	pdfkit.from_url('file:///C:/Users/Yash/Downloads/Form/js.html?student_name=Yash%20Rasniya&sem=4&year=2&roll_number=201340101047&fname=Vivek%20Uniyal&assignmentTitle=Practical%20File&subName=Theory%20Of%20Computation', 'out.pdf',options=options ,verbose=True)


	return ren
@app.route("/show")
def download_pdf():
	options = {
		'page-size': 'A4',
		'margin-top': '0.75in',
		'margin-right': '0.75in',
		'margin-bottom': '0.75in',
		'margin-left': '0.75in',
		'encoding': "UTF-8",
		'custom-header': [
			('Accept-Encoding', 'gzip')
		],
		'cookie': [
			('cookie-empty-value', '""'),
			('cookie-name1', 'cookie-value1'),
			('cookie-name2', 'cookie-value2'),
		],
		'no-outline': None
	}
	pdf=pdfkit.from_url("http://127.0.0.1:5000/pdf/Yash%20Rasniya/4/2/201340101047/Vivek%20Uniyal/Practical%20File/Theory%20Of%20Computation",
						options=options,verbose=True)
	responce = make_response(pdf)
	responce.headers['Content-Type'] = 'application/pdf'
	responce.headers['Content-Disposotion'] = 'inline;filename=output.pdf'

	return responce
if __name__ == "__main__":
    app.run(debug=True)