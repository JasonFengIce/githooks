require 'java'
require './libs/Email.jar'
include_class "javax.swing.JFrame"
include_class "javax.swing.JLabel"
include_class "org.apache.commons.mail.MultiPartEmail"
include_class "org.apache.commons.mail.DefaultAuthenticator"

frame = JFrame.new()
jlabel = JLabel.new("Hello from JRuby with Swing")
frame.getContentPane().add(jlabel)
# frame.content_pane.add(label)
frame.pack()
frame.setVisible(true)
frame.visible = true


emailMsg=`git log master ^origin/master`

email = MultiPartEmail.new()
email.setHostName("smtp.qiye.163.com");
email.setSslSmtpPort("25");
email.setAuthenticator(DefaultAuthenticator.new("fenghuibin@ismartv.cn", "Hope0Dies"));
email.setSSLOnConnect(true);
email.setFrom("fenghuibin@ismartv.cn");
email.setSubject("subject");
email.setMsg(emailMsg);
email.addTo("fenghuibin@ismartv.cn");
email.send();












