function sendEmail(){
    Email.send({
      Host : "smtp.gmail.com",
      Username : "provasitounimore4567@gmail.com",
      Password : "unimore.it",
      To : 'provasitounimore@gmail.com',
      From : document.getElementById("email").value,
      Subject : "Nuovo contatto from Just Wine",
      Body : "And this is the body" + document.getElementById("nome").value
      + "<br> Email: " + document.getElementById("email").value
      + "<br> Telefono: " + document.getElementById("Numero").value
      + "<br> Messaggio: " + document.getElementById("messaggio").value
  }).then(
    message => alert("Messaggio mandato correttamente! Presto verrai ricontattato.")
  );

  return false;
  }