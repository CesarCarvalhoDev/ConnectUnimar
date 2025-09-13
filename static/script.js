document.getElementById('submitButton').addEventListener('click', () => {
    // Perfil
    const nome = document.getElementById('nome').value;
    const idade = document.getElementById('idade').value;
    const cargo_atual = document.getElementById('cargo').value;
    const anos_experiencia = document.getElementById('anos').value;

    // Interesses
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

    // Habilidades
    const habilidades = {
        lideranca: parseInt(document.querySelector('input[name="habilidades_lideranca"]').value) || 0,
        negociacao: parseInt(document.querySelector('input[name="habilidades_negociacao"]').value) || 0,
        analise_dados: parseInt(document.querySelector('input[name="habilidades_analise_dados"]').value) || 0,
        criatividade: parseInt(document.querySelector('input[name="habilidades_criatividade"]').value) || 0,
        organizacao: parseInt(document.querySelector('input[name="habilidades_organizacao"]').value) || 0,
        atendimento_cliente: parseInt(document.querySelector('input[name="habilidades_atendimento_cliente"]').value) || 0,
        planejamento: parseInt(document.querySelector('input[name="habilidades_planejamento"]').value) || 0
    };

    // Objetivos
    const objetivos = {
        promocao: document.querySelector('input[name="objetivo_promocao"]').checked,
        melhorar_habilidades: document.querySelector('input[name="objetivo_melhorar_habilidades"]').checked,
        abrir_negocio: document.querySelector('input[name="objetivo_abrir_negocio"]').checked
    };

    // Criar objeto JSON completo
    const data = {
        perfil: { nome, idade, cargo_atual, anos_experiencia },
        interesses,
        habilidades,
        objetivos
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
        console.log(result);
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});
