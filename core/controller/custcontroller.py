from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from core.model.custmodel import Cust_details
import json

app = Blueprint('cust', __name__)

# displaying the mos personalia info..
@app.route('/contact')
def Contact():
    print('ín form')
    return render_template('contact.html')


@app.route('/contact_ajax')
def ContactAjax():
    print('ín form')
    return render_template('contact_ajax.html')    


@app.route('/contact_ajax_popup')
def contact_ajax_popup():
    print('ín form')
    return render_template('contact_ajax_popup.html')    
    
@app.route('/Post_contact_normal', methods = ["POST"])
def Post_contact_normal():
    if request.method == "POST":
        print('in post')
        # fetching data from form..
        data = {
            'contact_number' : request.form['contact_number'],
            'name' : request.form['name'],
           

        }

        #ceating object for model class..
        c = Cust_details()

        #calling insert method using that object..
        output = c.insert_cust(data)

        if output:
            flash('Successfully Saved ! ' )
            return redirect (url_for('cust.Custindex'))    


@app.route('/contact_index_ajax', methods = ["GET","POST"])
def contact_index_ajax():
    c = Cust_details()
    msg = ""
    status = 1;
    results = c.get_cust(); 
    html = render_template('customer_index_ajax.html',cust_data=results)

    return jsonify({'message': msg,'status' : status,'html':html})                


@app.route('/Post_contact_ajax', methods = ["POST"])
def Post_contact_ajax():
    c = Cust_details()
    msg = ""
    status = 0
    valid = True
    if request.method == "POST":
        print('in post')
        # fetching data from form..
        data = {
            'contact_number' : request.values.get('contact_number'),
            'name' : request.values.get('name'),
        }

        if data.get('name'):
            print(data.get('name'))
        else:    
            valid = False  
            msg = "Please Enter the Name"


        #ceating object for model class..

        if valid:
            #calling insert method using that object..
            output = c.insert_cust(data)
            if output:
                msg = "Successfully Saved !" 
                results = c.get_cust(); 
                html = render_template('customer_index_ajax.html',cust_data=results)
                status = 1
            else:
                msg = "failed" 
                status =0
       

        return jsonify({'message': msg,'status' : status,'html':html})    

@app.route('/mytest_ajax', methods = ["GET","POST"])
def mytest_ajax():
        name =    request.values.get("name")
        # name =  request.form['name']
        return jsonify({'message': "hi i am ajax from server",'status' : 1,'name':name})                        

@app.route('/post_contact', methods = ["GET","POST"])
def Post_contact():
    # if request.method == "POST":
    print('in post')

    # fetching data from form..
    data = {
        'contact_number' : request.values.get('contact_number'),
        'name' : request.values.get('name'),
        'interest' : request.values.get('interest'),
        'plan' : request.values.get('plan'),
        'societies' : request.values.get('check')

    }

    #ceating object for model class..
    c = Cust_details()

    #calling insert method using that object..
    output = c.insert_cust(data)

    if output:
        flash('Successfully Saved ! ' )
        return redirect (url_for('cust.Custindex'))
            

@app.route('/cust_index')
def Custindex():
    print('ín Index')
    c = Cust_details()
    output = c.get_cust() 
    print(output)
     # return all rows as a JSON array of objects
    # json_data = json.dumps([dict(r) for r in output])
    # print('Return data to Android ..')
    # print(json_data)        
    # return json_data
    # print(output.json())
    # return output.json()
    return render_template('customer_index.html',cust_data=output)

@app.route('/delete_contact/<int:id>' ,methods = ["GET","POST"])
def Delete_contact(id):
    print("Inside in contoller delete")
    print(id)
    id = int(id)
    # contact_id = request.args.get('contact_id')
    # print(contact_id)
    c = Cust_details()
    output = c.delete_cust(id) 
    print(output)
    flash('Customer Number'+ ' '+str(id)  +' ' +'is Deleted ! ' )
    return redirect (url_for('cust.Custindex'))

@app.route('/edit_contact/<int:id>',methods = ["GET","POST"])
def Edit_contact(id):
    print("Inside in contoller Edit")
    print(id)
    id = int(id)
    c = Cust_details()
    output = c.edit_cust(id) 
    print(output)
    # data_ = [dict(r) for r in output]
    print(output.name)
    # return all rows as a JSON array of objects
    # json_data = json.dumps([dict(r) for r in output])
    # print('Printing for results data to sent edit html file Boss ')
    # # results = json_data
    # print(json_data)
    # data  = json.loads(json_data)
    # contact_list = data[0]
    # print (contact_list)
    # print('Return data to Android ..')
    return render_template('edit_contact.html',result = output,id = id)
    # return (output)      
    # Post_Edit_contact    
    # 

@app.route('/post_edit_contact/<int:id>',methods = ["GET","POST"])
def Post_Edit_contact(id):
    print("Inside in contoller Post Edit")
    print(id)
    id = int(id)
    if request.method == "POST":
        print('in post Edit')

        # fetching data from form..
        data = {
             'contact_number' : request.form['contact_number'],
            'name' : request.form['name'],
            'interest' : request.form['interest'],
            'plan' : request.form['plan'],
        }

        #ceating object for model class..
        c = Cust_details()

        #calling insert method using that object..
        output = c.update_cust(id,data)
    # return all rows as a JSON array of objects
    # json_data = json.dumps([dict(r) for r in output])
    # results = json_data.json()
    # response = json.dumps(output)
    # print('Return data to Android ..')
    flash('Successfully Updated ! ' )
    return redirect (url_for('cust.Custindex'))        
    # return render_template('edit_contact.html',result=json_data)           



    