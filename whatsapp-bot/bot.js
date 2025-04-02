const venom = require('venom-bot');
const axios = require('axios');

venom
  .create({
    session: 'syron-session',
    headless: false, // usa navegador visível
    browserArgs: ['--no-sandbox']
  })

  .then((client) => start(client))
  .catch((erro) => {
    console.log(erro);
  });

function start(client) {
  client.onMessage(async (message) => {
    if (message.body && message.isGroupMsg === false) {
      const texto = message.body;

      try {
        const resposta = await axios.post('http://localhost:5000/comando', {
          comando: texto
        });

        const respostaSyron = resposta.data.resposta;
        client.sendText(message.from, respostaSyron);
      } catch (error) {
        client.sendText(message.from, 'Erro ao comunicar com o cérebro SYRON.');
      }
    }
  });
}
