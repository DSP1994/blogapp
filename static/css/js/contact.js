import emailjs from "emailjs-com";
import React from 'react';

export default function ContactMe(){
    function sendEmail(e){
        e.preventDefault();

        emailjs.sendForm('gmail', 'blog_contact', form.current, 'Z2Z1czOYifXldjts1')
          .then((result) => {
              console.log(result.text);
          }, (error) => {
              console.log(error.text);
          });
          e.target.reset()    
    }

    return(
        <div>
            <div className="container mt-5">
                <div className="Row">
                    <div className="col-md-6">
                        <form onSubmit={sendEmail}>
                            <div className="row pt-5 mx-auto">
                                <div className="col-8 form-group mx-auto">
                                    <input type="text" className="form-control" placeholder="Name" name="name"/>
                                </div>
                                <div className="col-8 pt-2 form-group mx-auto">
                                    <input type="text" className="form-control" placeholder="Subject" name="subject"/>
                                </div>
                                <div className="col-8 pt-2 form-group mx-auto">
                                    <textarea className="form-control" id="" cols="30" rows="8" placeholder="Your Message" name="message"></textarea>
                                </div>
                                <div className="col-8 pt-3 mx-auto">
                                    <input type="submit" className="btn btn-info" value="Send Message"></input>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}