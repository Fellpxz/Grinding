const form = document.querySelector('form');
const input = document.querySelector('#item');
const lista = document.querySelector('#lista-tarefas');

form.addEventListener('submit', (e) => {
  e.preventDefault(); // previne que a página seja recarregada ao enviar o form

  const texto = input.value.trim(); // remove espaços em branco no início e no fim da string

  if (texto !== '') {
    const li = document.createElement('li');
    const span = document.createElement('span');
    const botaoExcluir = document.createElement('button');

    span.textContent = texto;
    botaoExcluir.textContent = 'Excluir';

    li.appendChild(span);
    li.appendChild(botaoExcluir);
    lista.appendChild(li);

    input.value = ''; // limpa o campo de texto
  }
});

lista.addEventListener('click', (e) => {
  if (e.target.tagName === 'BUTTON') {
    const li = e.target.parentNode;
    lista.removeChild(li);
  }
});