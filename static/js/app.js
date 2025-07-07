let currentSubject = 'math';
let correctCount = 0;
let totalCount = 0;

function selectSubject(subj) {
  currentSubject = subj;
  loadQuestion(subj);
}

async function loadQuestion(subject) {
  const res = await fetch(`/question/${subject}`);
  if (!res.ok) {
    document.getElementById('question-text').textContent = 'Nepavyko gauti klausimo.';
    return;
  }
  const q = await res.json();
  document.getElementById('question-text').textContent = q.question;
  const diagram = document.getElementById('diagram');
  if (q.image) {
    diagram.src = `data:image/png;base64,${q.image}`;
    diagram.style.display = 'block';
  } else {
    diagram.style.display = 'none';
  }
  const optsDiv = document.getElementById('options');
  optsDiv.innerHTML = '';
  q.options.forEach(opt => {
    const btn = document.createElement('button');
    btn.textContent = opt;
    btn.onclick = () => checkAnswer(opt, q.answer, q.hint);
    optsDiv.appendChild(btn);
  });
  document.getElementById('feedback').textContent = '';
}

function checkAnswer(choice, answer, hint) {
  totalCount++;
  if (choice === answer) {
    correctCount++;
    document.getElementById('feedback').textContent = 'Teisingai!';
  } else {
    document.getElementById('feedback').textContent = `Neteisinga. Teisingas atsakymas: ${answer}. Užuomina: ${hint}`;
  }
  document.getElementById('next-btn').style.display = 'inline-block';
  updateProgress();
}

function updateProgress() {
  const p = Math.round((correctCount/totalCount)*100);
  document.title = `Progreso lygis: ${p}%`;
}

document.addEventListener('DOMContentLoaded', () => {
  loadQuestion(currentSubject);
});
