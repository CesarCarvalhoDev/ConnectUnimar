document.getElementById('submitButton').addEventListener('click', () => {
    const form = document.getElementById('userForm');

    // Pegar interesses
    const interesses = {
        gestao: parseInt(document.querySelector('input[name="interesses_gestao"]').value) || 0,
        marketing: parseInt(document.querySelector('input[name="interesses_marketing"]').value) || 0,
        financas: parseInt(document.querySelector('input[name="interesses_financas"]').value) || 0,
        tecnologia: parseInt(document.querySelector('input[name="interesses_tecnologia"]').value) || 0,
        vendas: parseInt(document.querySelector('input[name="interesses_vendas"]').value) || 0,
        inovacao: parseInt(document.querySelector('input[name="interesses_inovacao"]').value) || 0,
        rh: parseInt(document.querySelector('input[name="interesses_rh"]').value) || 0,
        estrategia: parseInt(document.querySelector('input[name="interesses_estrategia"]').value) || 0,
        operacoes: parseInt(document.querySelector('input[name="interesses_operacoes"]').value) || 0
    };

    // Pegar habilidades
    const habilidades = {
        lideranca: parseInt(document.querySelector('input[name="habilidades_lideranca"]').value) || 0,
        negociacao: parseInt(document.querySelector('input[name="habilidades_negociacao"]').value) || 0,
        analise_dados: parseInt(document.querySelector('input[name="habilidades_analise_dados"]').value) || 0,
        criatividade: parseInt(document.querySelector('input[name="habilidades_criatividade"]').value) || 0,
        organizacao: parseInt(document.querySelector('input[name="habilidades_organizacao"]').value) || 0,
        atendimento_cliente: parseInt(document.querySelector('input[name="habilidades_atendimento_cliente"]').value) || 0,
        planejamento: parseInt(document.querySelector('input[name="habilidades_planejamento"]').value) || 0
    };

    // Criar objeto completo
    const data = {
        perfil,
        interesses,
        habilidades
    };

    // Enviar JSON para o backend
    fetch('/save-json', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        alert('Dados enviados com sucesso!');
        window.location.href = '/resultado'; // Redireciona para a página de resultado
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});
