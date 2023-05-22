function format(sender, threadCount) {
  return sender + ": " + threadCount + " unread emails";
}

function sendEmail(content, recipientEmail) {
  var subject = "Gmail Senders";
  var body = content;
  MailApp.sendEmail(recipientEmail, subject, body);
}

function myFunction() {
  var startThread = 0;
  var stepSize = 50; // This is the step size. Vary it accordingly based on the number of emails you have!
  var senders = {};

  while (true) {
    var threads = GmailApp.getInboxThreads(
      startThread,
      stepSize
    );

    if (threads.length === 0) {
      break;
    }

    for (var j = 0; j < threads.length; j++) {
      var sender = threads[j].getMessages()[0].getFrom();

      if (sender in senders) {
        senders[sender]++;
      } else {
        senders[sender] = 1;
      }
    }

    startThread += threads.length;
    Logger.log("Done until " + startThread);
  }

  var sortedSenders = Object.entries(senders).sort((a, b) => b[1] - a[1]);
  var content = "";
  for (var i = 0; i < sortedSenders.length; i++) {
    var sender = sortedSenders[i][0];
    var threadCount = sortedSenders[i][1];
    content += format(sender, threadCount) + "\n";
  }

  var recipientEmail = "YOUR EMAIL"; // Update with the desired recipient email address
  sendEmail(content, recipientEmail);
  Logger.log("Finished!");
}
