import datetime
import json
from flask import Flask
from flask import render_template,request
#import request
from scrapeHandler import *
import logging
from communicationHandler import *


#RUNNING MODE
mode='HEROKU' #LOCAL




app = Flask(__name__)
app.debug = 1

@app.route('/',methods=['GET', 'POST'])
def search_start():  # put application's code here

    if request.method == 'POST':
        link = request.form.get('search_txt')

        com('user {} searched'.format(link))
        # Send result data to result_data HTML file
        com('\__Scrape initiated successfully')
        result = scarpe_and_stat(link+'recent-activity/shares/')
        #print(result)
        #print([result['mip'].to_html(classes='data', header="true")])
        render =render_template(
            'webpage/results_style_in_html.html',
            title="LI_data_roundup",
            date = ' '+str(datetime.datetime.now())[:10],
            user_name =  result['user_name'],
            followers = result['followers'],
            posts_in_tf=result['posts_in_tf'],
            avg_likes = result['avg_likes'],
            profile_redirect =link,
            avg_comments = result['avg_comments'],
            ttl_likes = result['ttl_likes'],
            ttl_comments = result['ttl_comments'],
            tables=[result['mip'].to_html(classes='data', header="true",index = False)],
            pp_url = result['pp_url'])

        file_name ='html_saves/'+result['user_name']+ ' '+str(datetime.datetime.now())[:10]+'.html'
        save_html = open(file_name , "w")
        save_html.write(render)
        save_html.close()

        #pdfkit.from_file(file_name, file_name[:-5]+'.pdf')

        #"""with open('/Users/dnsn/My Drive/json_db_files/' + result['user_name'] + ' ' + str(datetime.datetime.now())+'.json', "w")  as outfile:
        #    outfile.write(result)"""


        return render

    return render_template('webpage/search.html', title="LI_data_roundup")





@app.route('/passing', methods=['POST'])
def display():
    if request.method == 'POST':
        result = request.form.get('search_txt')
        # Send result data to result_data HTML file
        print(result)
    return'',204

#Egg
# IF NO RETURN WANTED::    return'', 204


if __name__ == '__main__':
    app.run(debug=True)








#https://www.linkedin.com/posts/sonja-windhager-5141971a4_netzwerk-reversementoring-rolemodel-activity-7011735175222964224-gi9o?utm_source=share&utm_medium=member_desktop
#https://www.linkedin.com/posts/sonja-windhager-5141971a4_personalbranding-insightconsulting-activity-6959868669657001984-nbZi/?utm_source=share&utm_medium=member_desktop
#https://www.linkedin.com/posts/sonja-windhager-5141971a4_bachelorabschluss-lebenskrise-activity-6951127668880789504-grnG?utm_source=share&utm_medium=member_desktop
#https://www.linkedin.com/posts/sonja-windhager-5141971a4_bachelorarbeit-praktikum-womeninleadership-activity-6937786137226678272-mFxP?utm_source=share&utm_medium=member_desktop
#https://www.linkedin.com/posts/sonja-windhager-5141971a4_learning-berufseinsteiger-perfektionismus-activity-6895441937034227712-q6CN?utm_source=share&utm_medium=member_desktop
#https://www.linkedin.com/posts/sonja-windhager-5141971a4_intership-socialmediamarketing-excited-activity-6894401389179527168-ddlc?utm_source=share&utm_medium=member_desktop
#https://www.linkedin.com/posts/sonja-windhager-5141971a4_learning-berufseinsteiger-perfektionismus-activity-6895441937034227712-q6CN?utm_source=share&utm_medium=member_desktop
#"https://www.lcom/premium/products/?upsellOrderOrigin=premium_nav_upsell_text&amp;destRedirectURL=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fsonja-windhager-5141971a4%2F"

"""user_name = "Erik fragger"
followers = 32123
avg_likes = 2322
avg_comments = 232
ttl_likes 29832
ttl_comments = 8748
pp_url = ''


transform:rotate(270deg);
  width:40px;
  position:fixed;
  top:10px;
  left:10px;
  height:50px; 
  border-radius:3px;
  text-align: center;
  text-justify: center;
  color:white;
  background-color:#1873C9;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
"""
