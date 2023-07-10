function groupUnreadEmailsBySenderAndSendEmail() {
  var totalThreads = 2000; // Total number of threads to retrieve
  var batchSize = 50; // Number of threads to process per batch
  var processedThreads = 0; // Counter for processed threads
  var senders = {};

  var labelToExclude = "to-read-newsletters"; // Replace "LabelName" with the label you want to exclude

  while (processedThreads < totalThreads) {
    var remainingThreads = totalThreads - processedThreads;
    var batchCount = Math.min(batchSize, remainingThreads);

    // Build the search query excluding the label
    var searchQuery = 'is:unread -label:' + labelToExclude;

    var threads = GmailApp.search(searchQuery, processedThreads, batchCount);

    for (var i = 0; i < threads.length; i++) {
      var messages = threads[i].getMessages();
      var sender = messages[0].getFrom();

      if (sender in senders) {
        senders[sender]++;
      } else {
        senders[sender] = 1;
      }
    }

    processedThreads += threads.length;
    Logger.log("Processed " + processedThreads + " out of " + totalThreads + " threads");
  }

  var sortedSenders = Object.entries(senders).sort((a, b) => b[1] - a[1]);

  var content = "";
  for (var i = 0; i < sortedSenders.length; i++) {
    var sender = sortedSenders[i][0];
    var emailCount = sortedSenders[i][1];
    content += sender + " - " + emailCount + " emails\n";
  }

  var recipientEmail = "YOUR_EMAIL"; // Update with the desired recipient email address
  var subject = "Grouped Unread Emails (Sorted)";
  var body = content;

  // Send the email
  GmailApp.sendEmail(recipientEmail, subject, body);
  Logger.log("Email sent to " + recipientEmail);
}
