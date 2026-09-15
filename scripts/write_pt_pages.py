#!/usr/bin/env python3
"""Write Portuguese translations of the homepage and two safety guides."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from i18n_chrome import render_page, write_page

HOME_CONTENT = r"""        <h1 class="page-title">Psilocibina</h1>
        <p class="page-subtitle">De WikiPsilocybin, a enciclopédia livre da psilocibina, atualizada diariamente</p>

        <div class="infobox">
            <div class="infobox-title">Psilocibina</div>
            <div class="infobox-image">
                <img src="https://d8j0ntlcm91z4.cloudfront.net/user_36uL1HV6CQZ9Ia0ikUE78jQJB98/hf_20260808_070842_c807ec80-0269-48c6-a459-06b22fa82a97.png" alt="Visualização molecular da psilocibina">
                <div class="caption">Ilustração da conectividade de uma rede neuronal (representação artística, não é uma imagem de pesquisa)</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Fórmula</div>
                <div class="infobox-value">C&#8321;&#8322;H&#8321;&#8327;N&#8322;O&#8324;P</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Massa molar</div>
                <div class="infobox-value">284.25 g/mol</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Primeiro isolamento</div>
                <div class="infobox-value">1958, por Albert Hofmann</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Espécies conhecidas</div>
                <div class="infobox-value">mais de 200 fungos</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Ensaios clínicos</div>
                <div class="infobox-value">mais de 400 registados</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Uso humano</div>
                <div class="infobox-value">~6.000 anos documentados</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Situação legal</div>
                <div class="infobox-value">Varia; Lista I (federal dos EUA), uso terapêutico legal em OR, CO, AU</div>
            </div>
        </div>

        <div id="recent-events" class="recent-events">
            <h3>Acontecimentos recentes</h3>
            <ul class="event-list">
                <li>
                    <span class="event-date">6 ago 2026</span>
                    <span class="event-tag tag-policy">Política</span>
                    <span class="event-link"><a href="/events/2026-08-06-va-pivot-trial/">VA launches PIVOT, a five-site randomized trial of psilocybin for veterans with treatment-resistant depression</a></span>
                </li>
                <li>
                    <span class="event-date">30 jul 2026</span>
                    <span class="event-tag tag-research">Pesquisa</span>
                    <span class="event-link"><a href="/events/2026-07-30-osu-veterans-ptsd-pilot/">Ohio State pilot trial: 9 of 12 veterans with severe, treatment-resistant PTSD in remission one month after psilocybin-assisted therapy</a></span>
                </li>
                <li>
                    <span class="event-date">26 jan 2026</span>
                    <span class="event-tag tag-culture">Cultura</span>
                    <span class="event-link"><a href="/events/2026-01-26-rand-psychedelic-use-survey/">RAND survey: about 11 million US adults used psilocybin in 2025, and most past-year users microdosed</a></span>
                </li>
                <li>
                    <span class="event-date">31 mar 2025</span>
                    <span class="event-tag tag-policy">Política</span>
                    <span class="event-link"><a href="/events/2025-03-31-colorado-first-healing-center/">Colorado issues its first licensed psilocybin healing center license to The Center Origin in Denver</a></span>
                </li>
                <li>
                    <span class="event-date">17 jul 2024</span>
                    <span class="event-tag tag-research">Pesquisa</span>
                    <span class="event-link"><a href="/events/2024-07-17-washu-psilocybin-desynchronizes-brain/">Washington University study in Nature shows psilocybin desynchronizes the brain's default mode network, with some changes lasting weeks</a></span>
                </li>
            </ul>
            <span class="view-all-link"><a href="/pt/events/">Ver todos os acontecimentos &rarr;</a></span>
        </div>

        <div class="toc">
            <div class="toc-title">Conteúdo</div>
            <ol>
                <li><a href="#what-is">O que é a psilocibina?</a></li>
                <li><a href="#how-it-works">Como atua</a></li>
                <li><a href="#research">Pesquisa e ensaios clínicos</a></li>
                <li><a href="#therapeutic">Aplicações terapêuticas</a></li>
                <li><a href="#microdosing">Microdose</a></li>
                <li><a href="#legal">Situação legal</a></li>
                <li><a href="#safety">Segurança e redução de danos</a></li>
            </ol>
        </div>

        <h2 id="what-is">O que é a psilocibina?</h2>
        <p>A psilocibina é um composto psicadélico de origem natural produzido por mais de 200 espécies de fungos, conhecidos habitualmente como «cogumelos mágicos». Após a ingestão, o corpo converte a psilocibina em psilocina, que interage com os recetores de serotonina do cérebro e produz estados alterados de consciência, alterações visuais e auditivas, e transformações profundas da perceção e do pensamento.</p>
        <p>Isolada e sintetizada pela primeira vez pelo químico suíço Albert Hofmann em 1958, a psilocibina tem sido usada em práticas cerimoniais indígenas durante milhares de anos. A evidência arqueológica sugere um uso humano de cogumelos com psilocibina que remonta pelo menos a 6.000 anos nas culturas mesoamericanas.</p>

        <h2 id="how-it-works">Como atua</h2>
        <p>A psilocibina é um profármaco: biologicamente inativa até o corpo a metabolizar. Após a ingestão, as enzimas fosfatase alcalina do intestino e do fígado removem um grupo fosfato e convertem a psilocibina em psilocina (4-hidroxi-N,N-dimetiltriptamina).</p>
        <p>O principal mecanismo de ação da psilocina é o agonismo dos recetores de serotonina 5-HT<sub>2A</sub> no córtex pré-frontal. Isto desencadeia uma cascata de efeitos:</p>
        <ul>
            <li><strong>Interrupção da rede neuronal por defeito (DMN)</strong>: reduz a atividade do sistema de «piloto automático» do cérebro e permite que se formem conexões neuronais novas</li>
            <li><strong>Maior conectividade neuronal</strong>: regiões cerebrais que habitualmente não comunicam começam a interagir e produzem experiências sinestésicas e associativas</li>
            <li><strong>Promoção da neuroplasticidade</strong>: estimula o crescimento dendrítico e a densidade sináptica, em particular no córtex pré-frontal e no hipocampo</li>
            <li><strong>Processamento emocional</strong>: aumenta a resposta da amígdala a estímulos emocionais e reduz a reatividade baseada no medo</li>
        </ul>
        <div class="ambox">
            <strong>Duração dos efeitos:</strong> O início ocorre habitualmente 20&ndash;40 minutos após a ingestão. Os efeitos máximos duram 2&ndash;3 horas, com uma duração total de 4&ndash;6 horas. Os efeitos residuais sobre o ânimo e a cognição podem persistir dias ou semanas.
        </div>

        <h2 id="research">Pesquisa e ensaios clínicos</h2>
        <p>A última década viu um ressurgimento sem precedentes da pesquisa sobre psilocibina, com instituições importantes como Johns Hopkins, Imperial College London, NYU e Yale a realizar ensaios clínicos rigorosos.</p>

        <h3>Marcos-chave da pesquisa</h3>
        <ul>
            <li><strong>2016:</strong> Johns Hopkins e NYU publicam em simultâneo estudos de referência que mostram que a psilocibina produz descidas substanciais e sustentadas da ansiedade e da depressão em doentes com cancro</li>
            <li><strong>2020:</strong> É criado o Johns Hopkins Center for Psychedelic &amp; Consciousness Research com 17 milhões de dólares de financiamento</li>
            <li><strong>2021:</strong> JAMA Psychiatry publica um ensaio aleatorizado que mostra que a terapia com psilocibina é pelo menos tão eficaz como o escitalopram (Lexapro) para o transtorno depressivo major</li>
            <li><strong>2023:</strong> A FDA concede a designação Breakthrough Therapy à terapia assistida com psilocibina para a depressão resistente ao tratamento</li>
            <li><strong>2024&ndash;2026:</strong> Múltiplos ensaios clínicos de fase 3 em curso ou concluídos para depressão, TEPT, dependência e mal-estar no fim de vida</li>
        </ul>
        <div class="ambox">
            <strong>Contagem atual de ensaios:</strong> Em 2026, há mais de 400 ensaios clínicos registados que envolvem psilocibina listados em ClinicalTrials.gov, que abrangem indicações desde a depressão major até à anorexia, às cefaleias em salvas e ao transtorno por uso de opioides.
        </div>

        <h2 id="therapeutic">Aplicações terapêuticas</h2>
        <p>A terapia assistida com psilocibina combina os efeitos farmacológicos da psilocibina com um apoio psicoterapêutico estruturado. A evidência atual apoia o seu potencial para tratar:</p>
        <ul>
            <li><strong>Transtorno depressivo major (MDD)</strong>: taxas de resposta de 60&ndash;80% em ensaios clínicos, com efeitos que duram 3&ndash;12 meses após 1&ndash;2 sessões</li>
            <li><strong>Depressão resistente ao tratamento (TRD)</strong>: designação Breakthrough Therapy da FDA concedida; ensaios de fase 3 em curso</li>
            <li><strong>Mal-estar no fim de vida</strong>: reduz a ansiedade existencial e a depressão em doentes com cancro terminal</li>
            <li><strong>TEPT</strong>: evidência emergente de estudos centrados em veteranos mostra uma redução significativa dos sintomas</li>
            <li><strong>Transtornos por uso de substâncias</strong>: resultados promissores para a cessação do tabaco e do álcool, com taxas de abandono 2&ndash;3 vezes superiores às dos tratamentos convencionais</li>
            <li><strong>Cefaleias em salvas</strong>: alívio comunicado por doentes e apoio clínico crescente</li>
        </ul>

        <h2 id="microdosing">Microdose</h2>
        <p>A microdose consiste em tomar doses subpercetuais de psilocibina: habitualmente 50&ndash;200 mg de material de cogumelo seco, ou cerca de 1/10 a 1/20 de uma dose completa. Quem a pratica comunica melhorias na criatividade, na concentração, na regulação emocional e no bem-estar geral sem experienciar efeitos psicadélicos.</p>
        <p>Embora a evidência anedótica seja abundante, a pesquisa controlada sobre microdose continua limitada. Entre os estudos destacados incluem-se:</p>
        <ul>
            <li>O estudo de autocegamento de 2022 da The Beckley Foundation, que concluiu que alguns benefícios persistiam mesmo no grupo placebo, o que sugere que os efeitos de expectativa desempenham um papel</li>
            <li>O estudo de 2023 da University of British Columbia que mostrou que quem tomava microdoses comunicava melhor ânimo e menos ansiedade do que quem não as tomava</li>
            <li>Ensaios em curso financiados pelo NIH que avaliam protocolos padronizados de microdose para o reforço cognitivo e os transtornos do ânimo</li>
        </ul>

        <h2 id="legal">Situação legal</h2>
        <p>O panorama legal da psilocibina evolui com rapidez em todo o mundo:</p>
        <h3>Estados Unidos</h3>
        <ul>
            <li><strong>Oregon</strong>: primeiro estado a legalizar a terapia regulada com psilocibina (Measure 109, 2020), com centros de serviço licenciados em funcionamento desde 2023</li>
            <li><strong>Colorado</strong>: a Proposition 122 (2022) despenalizou a psilocibina e criou um quadro de acesso regulado para uso terapêutico</li>
            <li><strong>Despenalização municipal</strong>: cidades como Denver, Oakland, Santa Cruz, Seattle, Detroit e outras retiraram prioridade à aplicação da lei</li>
            <li><strong>Federal</strong>: a psilocibina continua na Lista I da Controlled Substances Act, embora a legislação bipartidária para isenções de pesquisa continue a avançar</li>
        </ul>

        <h3>Internacional</h3>
        <ul>
            <li><strong>Canadá</strong>: o Special Access Program permite que os profissionais de saúde solicitem psilocibina para afecções resistentes ao tratamento</li>
            <li><strong>Austrália</strong>: a TGA aprovou a psilocibina para a depressão resistente ao tratamento em contextos de psiquiatras autorizados (julho de 2023)</li>
            <li><strong>Jamaica e Países Baixos</strong>: trufas/cogumelos de psilocibina disponíveis através de zonas cinzentas legais ou de legalidade explícita</li>
            <li><strong>União Europeia</strong>: vários países exploram quadros regulatórios; os ensaios clínicos expandem-se na Alemanha, no Reino Unido e na Suíça</li>
        </ul>

        <h2 id="safety">Segurança e redução de danos</h2>
        <p class="hatnote">Artigos principais: <a href="/pt/are-magic-mushrooms-dangerous/">Os cogumelos mágicos são perigosos?</a> e <a href="/pt/are-shrooms-addictive/">Os cogumelos viciam?</a></p>
        <p>A psilocibina tem um perfil de segurança bem estabelecido em comparação com outras substâncias psicoativas. A sua dose letal estimada é cerca de 1.000 vezes uma dose eficaz típica, não se documentou de forma fiável nenhuma sobredosagem mortal por psilocibina isolada num adulto saudável, não produz dependência física nem abstinência, e a tolerância rápida desencoraja o uso frequente. A análise multicritério de 2010 na <em>Lancet</em> de David Nutt e colegas classificou os cogumelos de psilocibina como os menos prejudiciais de 20 drogas recreativas ao considerar tanto o dano aos utilizadores como o dano a terceiros.</p>
        <p>Os riscos que existem são sobretudo psicológicos e situacionais, mais do que tóxicos:</p>
        <ul>
            <li><strong>Más viagens</strong>: ansiedade aguda, pânico ou confusão; num inquérito de quase 2.000 experiências difíceis, 11% das pessoas inquiridas puseram-se a si ou a outras em risco físico e 7.6% procuraram depois tratamento por sintomas persistentes</li>
            <li><strong>Vulnerabilidade psiquiátrica</strong>: não se recomenda a pessoas com antecedentes pessoais ou familiares de transtornos psicóticos ou bipolar I</li>
            <li><strong>Interações medicamentosas</strong>: o lítio associa-se a convulsões quando combinado com psicadélicos; os ISRS atenuam os efeitos; os IMAO podem intensificá-los</li>
            <li><strong>Cardiovascular</strong>: aumentos moderados e transitórios da frequência cardíaca e da pressão arterial; precaução com doença cardíaca preexistente</li>
            <li><strong>Identificação errada</strong>: espécies mortais de <em>Amanita</em> e <em>Galerina</em> podem parecer-se com os cogumelos de psilocibina; os cogumelos colhidos são a principal fonte de envenenamentos mortais por «cogumelos mágicos»</li>
            <li><strong>Set e setting</strong>: um acompanhante sóbrio, um ambiente privado seguro e uma dose conservadora são as salvaguardas mais eficazes</li>
        </ul>
        <div class="ambox">
            <strong>Precisa de ajuda agora?</strong> US Poison Control 1-800-222-1222 (gratuito, confidencial, 24/7) &middot; Fireside Project apoio entre pares psicadélico 62-FIRESIDE (623-473-7433) &middot; 988 Suicide &amp; Crisis Lifeline. Para o detalhe completo e as referências, veja <a href="/pt/are-magic-mushrooms-dangerous/">Os cogumelos mágicos são perigosos?</a>
        </div>
"""

DANGER_CONTENT = r"""        <h1 class="page-title">Os cogumelos mágicos são perigosos?</h1>
        <p class="page-subtitle">De WikiPsilocybin, a enciclopédia livre da psilocibina, um artigo de redução de danos</p>
        <p class="hatnote">Este artigo cobre os riscos, os efeitos secundários e a segurança dos cogumelos de psilocibina («cogumelos» ou «shrooms»). Sobre o composto em si, veja <a href="/pt/">Psilocibina</a>. Sobre dependência e potencial de abuso, veja <a href="/pt/are-shrooms-addictive/">Os cogumelos viciam?</a></p>
        <div class="infobox">
            <div class="infobox-title">Segurança dos cogumelos de psilocibina</div>
            <div class="infobox-row"><div class="infobox-label">Toxicidade física</div><div class="infobox-value">Muito baixa; a proporção dose letal/dose eficaz estima-se perto de 1,000:1<sup class="ref"><a href="#ref3">[3]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Mortes confirmadas por psilocibina isolada</div><div class="infobox-value">Praticamente nenhuma na literatura; as mortes implicam cogumelos tóxicos mal identificados, acidentes ou drogas coingeridas<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Principais riscos</div><div class="infobox-value">Mal-estar psicológico («má viagem»), conduta de risco sob os efeitos, psicose em pessoas vulneráveis, interações medicamentosas, identificação errada de cogumelos</div></div>
            <div class="infobox-row"><div class="infobox-label">Classificação global de dano</div><div class="infobox-value">A mais baixa de 20 drogas na análise multicritério da <em>Lancet</em> de 2010<sup class="ref"><a href="#ref1">[1]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Poison Control (EUA)</div><div class="infobox-value">1-800-222-1222</div></div>
        </div>
        <p><strong>Os cogumelos mágicos estão entre as drogas recreativas fisicamente menos perigosas que se estudaram, mas não estão isentos de risco.</strong> Os perigos principais são psicológicos mais do que toxicológicos: experiências aterradoras ou desestabilizadoras, acidentes sob os efeitos e o desencadear de psicose em pessoas com antecedentes pessoais ou familiares de transtornos psicóticos. Um perigo distinto e pouco apreciado é comer o cogumelo errado, já que várias espécies mortais se parecem com as que contêm psilocibina.<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref6">[6]</a></sup></p>
        <p>Na análise multicritério da <em>Lancet</em> de 2010 dirigida por David Nutt, os cogumelos de psilocibina obtiveram a pontuação mais baixa de dano combinado a utilizadores e a terceiros de 20 drogas, abaixo da cannabis, do álcool, do tabaco e de todas as outras substâncias avaliadas.<sup class="ref"><a href="#ref1">[1]</a></sup> Uma revisão de 2011 encomendada para a política de drogas neerlandesa chegou a uma conclusão semelhante e descreveu o potencial de dano físico e psicológico dos cogumelos mágicos como baixo.<sup class="ref"><a href="#ref2">[2]</a></sup> Este artigo expõe o que a evidência mostra de facto, onde estão os riscos reais e como os reduzir.</p>
        <div class="toc">
            <div class="toc-title">Conteúdo</div>
            <ol>
                <li><a href="#short-answer">A resposta breve</a></li>
                <li><a href="#side-effects">Efeitos secundários</a></li>
                <li><a href="#bad-trips">Más viagens e risco psicológico</a></li>
                <li><a href="#mental-health">Saúde mental, psicose e HPPD</a></li>
                <li><a href="#overdose">É possível uma sobredosagem? Toxicidade e envenenamento</a></li>
                <li><a href="#emergency">Sintomas de emergência</a></li>
                <li><a href="#interactions">Interações medicamentosas</a></li>
                <li><a href="#brain">Efeitos no cérebro</a></li>
                <li><a href="#who-should-avoid">Quem deve evitar a psilocibina</a></li>
                <li><a href="#harm-reduction">Redução de danos</a></li>
                <li><a href="#risks-benefits">Riscos face a benefícios</a></li>
                <li><a href="#references">Referências</a></li>
            </ol>
        </div>
        <h2 id="short-answer">A resposta breve</h2>
        <p>Quão perigosos são os cogumelos? No plano físico, muito pouco. A psilocibina não tem toxicidade orgânica conhecida nas doses que se tomam, não deprime a respiração, e a dose estimada necessária para matar uma pessoa é da ordem de mil vezes uma dose eficaz típica.<sup class="ref"><a href="#ref3">[3]</a></sup> Não se documentou nenhum caso fiável de sobredosagem mortal por cogumelos de psilocibina isolados num adulto saudável; o punhado de mortes na literatura implicou espécies tóxicas de aspeto semelhante, doença cardíaca preexistente, outras drogas ou acidentes como quedas e afogamentos sob intoxicação.<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup></p>
        <p>No plano psicológico, o panorama é mais matizado. No inquérito mais amplo de experiências difíceis com psilocibina, 39% de quase 2.000 pessoas inquiridas classificaram a sua pior «má viagem» entre as cinco experiências mais difíceis da vida, 11% disseram que se puseram a si ou a outras em risco de dano físico durante o episódio, e 7.6% procuraram tratamento por sintomas psicológicos persistentes depois.<sup class="ref"><a href="#ref7">[7]</a></sup> A maioria desses episódios ocorreu sem um acompanhante sóbrio, em ambientes não planeados ou a doses altas.</p>
        <div class="ambox">
            <strong>Em síntese:</strong> o perigo dos cogumelos mágicos vem sobretudo do <em>que as pessoas fazem sob os efeitos</em>, de <em>quem os toma</em> (pessoas vulneráveis à psicose), do <em>que mais há no organismo</em> (lítio, certas outras drogas) e de <em>se o cogumelo é realmente psilocibina</em>. Cada um desses riscos pode reduzir-se de forma substancial.
        </div>
        <h2 id="side-effects">Efeitos secundários</h2>
        <p>Os efeitos secundários dos cogumelos mágicos agrupam-se em três categorias: físicos, percetivos e psicológicos. Os efeitos agudos começam 20&ndash;40 minutos após a ingestão, atingem o máximo cerca de 60&ndash;90 minutos e resolvem-se em aproximadamente seis horas.<sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <table class="wikitable">
            <tr><th>Tipo</th><th>Efeitos habituais</th><th>Notas</th></tr>
            <tr><td>Físicos</td><td>Náuseas, vómitos (habitualmente no início), dilatação pupilar, aumentos modestos da frequência cardíaca e da pressão arterial, sudorese, arrepios, fraqueza muscular, má coordenação, bocejos</td><td>Em ensaios controlados, a pressão arterial e a frequência cardíaca sobem de forma moderada e voltam à linha de base em horas; as náuseas são a queixa mais frequente.<sup class="ref"><a href="#ref8">[8]</a></sup><sup class="ref"><a href="#ref9">[9]</a></sup></td></tr>
            <tr><td>Percetivos</td><td>Distorção visual e padrões, sentido alterado do tempo, sinestesia, intensificação do som e da cor</td><td>Dependentes da dose; efeitos esperados, não eventos adversos em si.</td></tr>
            <tr><td>Psicológicos</td><td>Euforia, assombro, riso, abertura emocional; também ansiedade, medo, paranoia, confusão, sensação de perda de controlo</td><td>Num estudo de dose alta de Johns Hopkins, cerca de um terço das pessoas voluntárias experienciou medo ou ansiedade significativos em algum momento da sessão, mesmo com uma preparação cuidadosa.<sup class="ref"><a href="#ref10">[10]</a></sup></td></tr>
            <tr><td>Dia seguinte</td><td>Fadiga, dor de cabeça, ânimo baixo ou, ao contrário, ânimo elevado («afterglow»)</td><td>A dor de cabeça após a psilocibina está relacionada com a dose, começa depois dos efeitos agudos e resolve-se em um ou dois dias.<sup class="ref"><a href="#ref11">[11]</a></sup></td></tr>
        </table>
        <p>Uma análise agrupada de 110 pessoas voluntárias saudáveis em oito estudos de laboratório suíços concluiu que a psilocibina em doses de até 0.315 mg/kg não produziu dano percetivo, psicológico nem físico persistente em nenhuma pessoa participante durante o seguimento.<sup class="ref"><a href="#ref9">[9]</a></sup></p>
        <h2 id="bad-trips">Más viagens e risco psicológico</h2>
        <p>Uma «má viagem» é um episódio agudo de ansiedade intensa, pânico, paranoia, disforia ou desorientação durante os efeitos da substância. É a experiência adversa grave mais habitual associada aos cogumelos mágicos e o motivo usual pelo qual as pessoas recorrem aos serviços de urgência.<sup class="ref"><a href="#ref12">[12]</a></sup> As más viagens estão fortemente ligadas à dose, ao estado mental («set») e ao ambiente («setting»).<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <p>O inquérito de 2016 de Carbonaro e colegas de 1,993 pessoas que tinham tido uma viagem difícil com psilocibina concluiu:<sup class="ref"><a href="#ref7">[7]</a></sup></p>
        <ul>
            <li>A dose mediana na pior experiência foi de cerca de 4 gramas de cogumelos secos, aproximadamente uma dose alta.</li>
            <li>11% puseram-se a si ou a outras pessoas em risco de dano físico; 2.6% agiram de forma agressiva ou violenta; 2.7% procuraram ajuda médica durante o episódio.</li>
            <li>Três pessoas inquiridas com ansiedade, depressão ou ideação suicida preexistentes tentaram o suicídio durante a experiência.</li>
            <li>7.6% procuraram tratamento por sintomas psicológicos persistentes depois.</li>
            <li>Apesar disso, 84% disseram que beneficiaram da experiência, e a dificuldade associou-se de forma positiva ao significado pessoal comunicado.</li>
        </ul>
        <p>Estar sozinho, estar num lugar desconhecido ou público e tomar uma dose maior do que a prevista tornaram o dano mais provável. Essas são as variáveis que a prática de redução de danos visa.</p>
        <h2 id="mental-health">Saúde mental, psicose e HPPD</h2>
        <p>O risco psiquiátrico mais grave é precipitar um episódio psicótico prolongado em alguém predisposto a transtornos psicóticos como a esquizofrenia ou o transtorno bipolar I. Os ensaios clínicos excluem essas pessoas participantes, de modo que faltam dados prospetivos sobre este grupo; a exclusão em si reflete um consenso de que o risco é real.<sup class="ref"><a href="#ref13">[13]</a></sup><sup class="ref"><a href="#ref14">[14]</a></sup> Relatos de casos descrevem psicose, mania e desestabilização anímica prolongada após o uso de cogumelos, habitualmente em pessoas com antecedentes pessoais ou familiares destas afecções.<sup class="ref"><a href="#ref14">[14]</a></sup></p>
        <p>Para a população geral, os grandes estudos epidemiológicos não concluíram que o uso de psicadélicos eleve a taxa de problemas de saúde mental. Uma análise de 130,152 adultos dos EUA na National Survey on Drug Use and Health não encontrou associação entre o uso de psicadélicos ao longo da vida (incluída a psilocibina) e o mal-estar psicológico grave, o tratamento de saúde mental ou os sintomas de pânico, depressão, ansiedade ou psicose; algumas associações iam na direção protetora.<sup class="ref"><a href="#ref15">[15]</a></sup> Uma análise de seguimento de 190,000 adultos encontrou de forma semelhante taxas mais baixas de mal-estar psicológico e de suicidalidade no mês anterior entre quem usava psicadélicos clássicos.<sup class="ref"><a href="#ref16">[16]</a></sup> Estes são achados correlacionais e não podem descartar o risco em subgrupos vulneráveis.</p>
        <p><strong>Transtorno percetivo persistente por alucinogénios (HPPD)</strong>, em que alterações visuais como rasto, halos ou neve visual persistem semanas ou anos, é um diagnóstico reconhecido do DSM-5. Parece ser raro, associa-se com mais frequência ao LSD do que à psilocibina e não ocorreu em nenhuma pessoa participante da literatura moderna de ensaios controlados, embora os inquéritos populacionais sugiram que os fenómenos transitórios de «flashback» não são raros e costumam desaparecer.<sup class="ref"><a href="#ref17">[17]</a></sup></p>
        <h2 id="overdose">É possível uma sobredosagem? Toxicidade e envenenamento</h2>
        <p>Uma «sobredosagem» de cogumelos mágicos no sentido de uma dose tóxica que põe a vida em perigo não é uma preocupação prática. A análise comparativa de Robert Gable estimou a dose letal de psilocibina em humanos em cerca de 1,000 vezes a dose eficaz, face a cerca de 10 para o álcool e 6 para a heroína intravenosa.<sup class="ref"><a href="#ref3">[3]</a></sup> Os estudos em animais situam a dose letal mediana de psilocibina em torno de 280 mg/kg em ratos, centenas de vezes a dose ativa humana por quilograma.<sup class="ref"><a href="#ref2">[2]</a></sup> Como um cogumelo seco contém aproximadamente 0.5&ndash;1% de psilocibina em peso, atingir uma quantidade fisicamente letal a comer cogumelos considera-se na prática impossível.<sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref4">[4]</a></sup></p>
        <p>O que as pessoas costumam querer dizer com «sobredosagem» é tomar muito mais do que o previsto, o que produz uma experiência avassaladora e aterradora mais do que dano orgânico. Os sintomas de uma dose muito alta incluem confusão grave, incapacidade de comunicar, agitação, pânico, vómitos e, em casos raros, convulsões ou temperatura alta, isto último comunicado com mais frequência quando havia outras substâncias envolvidas.<sup class="ref"><a href="#ref12">[12]</a></sup></p>
        <h3>Envenenamento por cogumelos mal identificados</h3>
        <p>O cenário genuinamente letal que envolve «cogumelos mágicos» é comer uma espécie tóxica por engano. As espécies mortais de <em>Amanita</em> e <em>Galerina</em>, que contêm amatoxinas que destroem o fígado, podem crescer nos mesmos habitats e parecer-se de forma superficial com algumas espécies de <em>Psilocybe</em>. O envenenamento por amatoxinas é enganador: os sintomas gastrointestinais aparecem 6&ndash;24 horas após a ingestão, parecem melhorar e depois desenvolve-se insuficiência hepática nos dias seguintes.<sup class="ref"><a href="#ref6">[6]</a></sup> Qualquer cogumelo comido do meio silvestre que produza vómitos e diarreia retardados muitas horas depois é uma emergência médica, não uma má viagem.</p>
        <p>As exposições a psilocibina comunicadas aos centros de toxicologia dos EUA aumentaram de forma acentuada no início da década de 2020, com um incremento de mais do triplo entre adolescentes entre 2018 e 2022, e cerca de três quartos dos casos adolescentes necessitaram de atenção médica.<sup class="ref"><a href="#ref18">[18]</a></sup> A maioria dos efeitos comunicados foram alucinações, agitação e taquicardia; os desfechos graves foram pouco frequentes.</p>
        <h3>Casos graves raros</h3>
        <p>Um número pequeno de relatos de casos descreve dano físico grave após o uso de cogumelos, incluída rabdomiólise com lesão renal aguda, e uma paragem cardíaca mortal numa pessoa recetora de um transplante de coração cujo coração transplantado não pôde responder com normalidade aos efeitos autonómicos da substância.<sup class="ref"><a href="#ref5">[5]</a></sup> As complicações renais e cardíacas associam-se com mais força a outros géneros de cogumelos (por exemplo <em>Cortinarius</em>) e a drogas coingeridas do que à psilocibina em si.<sup class="ref"><a href="#ref4">[4]</a></sup> Documentam-se aqui porque existem, não porque sejam típicas.</p>
        <h2 id="emergency">Sintomas de emergência</h2>
        <div class="ambox warn">
            <strong>Ligue para o 911 ou para o Poison Control (1-800-222-1222) se a pessoa:</strong> não responde ou não se consegue despertar; tem uma convulsão; tem dor torácica, um batimento muito rápido ou irregular, ou dificuldade para respirar; tem uma temperatura corporal alta com músculos rígidos ou sudorese profusa (possível toxicidade serotoninérgica, sobretudo se há outras drogas envolvidas); é violenta, se autolesiona ou tenta ir-se para um lugar perigoso; ou desenvolve vómitos e diarreia <em>horas depois</em> de comer cogumelos colhidos (possível envenenamento por amatoxinas).
        </div>
        <p>Uma pessoa que está assustada, confusa, chora ou está convencida de que algo corre mal, mas que está fisicamente estável, não costuma necessitar de uma ambulância. O que ajuda é um acompanhante sereno, um espaço quieto e seguro, a tranquilidade de que os efeitos são temporários e passarão em umas horas, e evitar a contenção ou a discussão.<sup class="ref"><a href="#ref19">[19]</a></sup> Em caso de dúvida, ligue para o Poison Control; o serviço é gratuito, confidencial e pode aconselhar se se necessita de atenção hospitalar.</p>
        <h2 id="interactions">Interações medicamentosas</h2>
        <ul>
            <li><strong>Lítio</strong>: a interação documentada mais importante. Numa análise de 62 relatos em linha de psicadélicos clássicos combinados com lítio, 47% implicaram convulsões e 18% necessitaram de atenção médica de urgência; a lamotrigina não mostrou esse padrão.<sup class="ref"><a href="#ref20">[20]</a></sup> A psilocibina não deve combinar-se com lítio.</li>
            <li><strong>ISRS e IRSN</strong>: os antidepressivos costumam atenuar os efeitos subjetivos da psilocibina mais do que produzir efeitos perigosos; a síndrome serotoninérgica por psilocibina isolada não está documentada, mas é uma preocupação teórica quando se combina com IMAO ou tramadol.<sup class="ref"><a href="#ref21">[21]</a></sup></li>
            <li><strong>IMAO</strong>: os inibidores da monoamina oxidase podem intensificar e prolongar os efeitos da psilocina de forma imprevisível.<sup class="ref"><a href="#ref21">[21]</a></sup></li>
            <li><strong>Álcool e cannabis</strong>: ambos aumentam a probabilidade de náuseas, confusão e uma experiência difícil; o álcool acrescenta risco de lesões.<sup class="ref"><a href="#ref12">[12]</a></sup></li>
            <li><strong>Estimulantes</strong>: a combinação com anfetaminas, MDMA ou cocaína eleva ainda mais a frequência cardíaca e a pressão arterial e aumenta o risco de ansiedade e hipertermia.</li>
        </ul>
        <h2 id="brain">Efeitos no cérebro</h2>
        <p>Os efeitos da psilocibina no cérebro são o tema do artigo principal do site; aqui a pergunta é se esses efeitos são prejudiciais. A psilocina atua sobretudo nos recetores de serotonina 5-HT<sub>2A</sub>, reduz de forma transitória a integridade da rede neuronal por defeito e aumenta a comunicação entre redes cerebrais que habitualmente estão segregadas.<sup class="ref"><a href="#ref22">[22]</a></sup> Um estudo de 2024 na <em>Nature</em> concluiu que uma só dose alta dessincronizou as redes corticais durante a duração dos efeitos da substância, com uma alteração menor na conexão hipocampo-rede por defeito que persistiu semanas.<sup class="ref"><a href="#ref23">[23]</a></sup></p>
        <p>Estas alterações consideram-se a base tanto da experiência aguda como dos efeitos terapêuticos comunicados, e nenhum estudo encontrou evidência de que a psilocibina danifique os neurónios. Os estudos em animais e em células sugerem o contrário: maior densidade de espinhas dendríticas e expressão de genes relacionados com a neuroplasticidade.<sup class="ref"><a href="#ref24">[24]</a></sup> Se estes efeitos de plasticidade poderiam ser prejudiciais num cérebro em desenvolvimento é desconhecido; quase não há dados controlados em adolescentes, o que é uma das razões pelas quais se desaconselha o uso em jovens.<sup class="ref"><a href="#ref18">[18]</a></sup></p>
        <h2 id="who-should-avoid">Quem deve evitar a psilocibina</h2>
        <p>A partir dos critérios de exclusão usados nos ensaios clínicos e das diretrizes de segurança publicadas:<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <ul>
            <li>Pessoas com antecedentes pessoais ou de familiar de primeiro grau de esquizofrenia, transtorno esquizoafetivo, transtorno bipolar I ou outras afecções psicóticas.</li>
            <li>Pessoas que tomam lítio, ou quem está com IMAO.</li>
            <li>Pessoas com hipertensão não controlada, AVC ou enfarte recente, arritmia grave ou outra doença cardiovascular significativa, pelo aumento transitório da pressão arterial e da frequência cardíaca.</li>
            <li>Pessoas grávidas ou que amamentam (não há dados de segurança).</li>
            <li>Adolescentes e crianças.</li>
            <li>Qualquer pessoa que esteja em crise aguda, gravemente intoxicada ou sem um lugar seguro e uma pessoa com quem estar.</li>
        </ul>
        <h2 id="harm-reduction">Redução de danos</h2>
        <p>As seguintes medidas abordam as fontes documentadas de dano. Extraem-se das diretrizes de segurança clínica<sup class="ref"><a href="#ref13">[13]</a></sup>, da literatura de inquéritos sobre experiências difíceis<sup class="ref"><a href="#ref7">[7]</a></sup> e de organizações de redução de danos como o Zendo Project e DanceSafe.<sup class="ref"><a href="#ref19">[19]</a></sup></p>
        <ol>
            <li><strong>Saiba o que tem.</strong> Nunca coma cogumelos colhidos a menos que uma pessoa identificadora competente tenha confirmado a espécie. A identificação errada é o único cenário com mais probabilidade de ser mortal.</li>
            <li><strong>Faça um rastreio.</strong> Reveja as contraindicações anteriores com honestidade, incluídos os antecedentes familiares e os medicamentos atuais.</li>
            <li><strong>Comece por baixo.</strong> A potência varia várias vezes entre espécies e mesmo entre lotes. Uma primeira dose de 1 grama ou menos de <em>Psilocybe cubensis</em> seco dá uma ideia do efeito; a mediana do inquérito para as piores experiências foi de cerca de 4 gramas.</li>
            <li><strong>Tenha um acompanhante sóbrio.</strong> Uma pessoa de confiança e sóbria que possa tranquilizar, reorientar e pedir ajuda se for preciso é a salvaguarda mais eficaz contra o dano durante uma má viagem.</li>
            <li><strong>Escolha o ambiente.</strong> Privado, familiar, a salvo do trânsito, da água, das alturas e da maquinaria pesada. Não conduza. Planeie ficar no mesmo sítio durante seis horas.</li>
            <li><strong>Não misture.</strong> Sobretudo não com lítio, álcool ou estimulantes.</li>
            <li><strong>Prepare-se para a dificuldade.</strong> A ansiedade e o medo são habituais e passam. Respirar devagar, mudar de quarto, mudar a música e que lhe recordem que a substância se desvanecerá são os apoios habituais. «Confie, largue, abra-se» é a frase usada nas sessões de Johns Hopkins.<sup class="ref"><a href="#ref10">[10]</a></sup></li>
            <li><strong>Saiba quando ligar.</strong> Veja os sintomas de emergência anteriores. O Poison Control não envolve as forças da ordem.</li>
            <li><strong>Integre depois.</strong> Falar da experiência com uma pessoa de confiança ou um terapeuta reduz a probabilidade de mal-estar persistente.</li>
        </ol>
        <h2 id="risks-benefits">Riscos face a benefícios</h2>
        <p>Os riscos e benefícios da psilocibina ponderam-se cada vez mais de forma formal. Do lado do benefício, os ensaios aleatorizados comunicaram grandes reduções da depressão,<sup class="ref"><a href="#ref25">[25]</a></sup> e reduções do consumo intenso de álcool no transtorno por uso de álcool,<sup class="ref"><a href="#ref26">[26]</a></sup> habitualmente após uma ou duas doses supervisionadas. Do lado do risco, os mesmos ensaios comunicam ansiedade transitória, dor de cabeça, náuseas e elevação da pressão arterial, e muito de vez em quando mal-estar prolongado. Em ambientes supervisionados com rastreio médico, nenhum ensaio comunicou uma morte, uma psicose persistente ou um caso de HPPD.<sup class="ref"><a href="#ref9">[9]</a></sup><sup class="ref"><a href="#ref25">[25]</a></sup></p>
        <p>Esses resultados não se transferem de forma direta ao uso não supervisionado, onde faltam o rastreio, a precisão da dose e o apoio que produzem o historial de segurança. O fosso entre a segurança clínica e o risco no mundo real é precisamente o que a redução de danos tenta fechar.</p>
        <h2 id="see-also">Ver também</h2>
        <div class="see-also">
        <ul>
            <li><a href="/pt/">Psilocibina</a>: panorama, farmacologia, pesquisa e situação legal</li>
            <li><a href="/pt/are-shrooms-addictive/">Os cogumelos viciam?</a>: dependência, tolerância e potencial de abuso</li>
            <li><a href="/pt/events/">Acontecimentos recentes</a>: notícias de pesquisa e política</li>
        </ul>
        </div>
<div class="ambox help">
            <strong>Se alguém precisa de ajuda agora mesmo:</strong> US Poison Control <strong>1-800-222-1222</strong> (24/7, gratuito, confidencial) &middot; Emergências <strong>911</strong> &middot; Linha de apoio entre pares psicadélico de Fireside Project <strong>62-FIRESIDE (623-473-7433)</strong> &middot; 988 Suicide &amp; Crisis Lifeline: ligue ou envie uma mensagem de texto para o <strong>988</strong>.
        </div>
        <h2 id="references">Referências</h2>
        <div class="refs">
        <ol>
            <li id="ref1">Nutt DJ, King LA, Phillips LD. Drug harms in the UK: a multicriteria decision analysis. <em>Lancet</em>. 2010;376(9752):1558&ndash;1565. <a href="https://doi.org/10.1016/S0140-6736(10)61462-6">doi:10.1016/S0140-6736(10)61462-6</a></li>
            <li id="ref2">van Amsterdam J, Opperhuizen A, van den Brink W. Harm potential of magic mushroom use: a review. <em>Regul Toxicol Pharmacol</em>. 2011;59(3):423&ndash;429. <a href="https://doi.org/10.1016/j.yrtph.2011.01.006">doi:10.1016/j.yrtph.2011.01.006</a></li>
            <li id="ref3">Gable RS. Comparison of acute lethal toxicity of commonly abused psychoactive substances. <em>Addiction</em>. 2004;99(6):686&ndash;696. <a href="https://doi.org/10.1111/j.1360-0443.2004.00744.x">doi:10.1111/j.1360-0443.2004.00744.x</a></li>
            <li id="ref4">Johnson MW, Griffiths RR, Hendricks PS, Henningfield JE. The abuse potential of medical psilocybin according to the 8 factors of the Controlled Substances Act. <em>Neuropharmacology</em>. 2018;142:143&ndash;166. <a href="https://doi.org/10.1016/j.neuropharm.2018.05.012">doi:10.1016/j.neuropharm.2018.05.012</a></li>
            <li id="ref5">Lim TH, Wasywich CA, Ruygrok PN. A fatal case of "magic mushroom" ingestion in a heart transplant recipient. <em>Intern Med J</em>. 2012;42(11):1268&ndash;1269. <a href="https://doi.org/10.1111/j.1445-5994.2012.02955.x">doi:10.1111/j.1445-5994.2012.02955.x</a>; Bickel M, Ditting T, Watz H, et al. Severe rhabdomyolysis, acute renal failure and posterior encephalopathy after "magic mushroom" abuse. <em>Eur J Emerg Med</em>. 2005;12(6):306&ndash;308. <a href="https://doi.org/10.1097/00063110-200512000-00011">doi:10.1097/00063110-200512000-00011</a></li>
            <li id="ref6">Diaz JH. Amatoxin-containing mushroom poisonings: species, toxidromes, treatments, and outcomes. <em>Wilderness Environ Med</em>. 2018;29(1):111&ndash;118. <a href="https://doi.org/10.1016/j.wem.2017.10.002">doi:10.1016/j.wem.2017.10.002</a></li>
            <li id="ref7">Carbonaro TM, Bradstreet MP, Barrett FS, et al. Survey study of challenging experiences after ingesting psilocybin mushrooms: acute and enduring positive and negative consequences. <em>J Psychopharmacol</em>. 2016;30(12):1268&ndash;1278. <a href="https://doi.org/10.1177/0269881116662634">doi:10.1177/0269881116662634</a></li>
            <li id="ref8">Passie T, Seifert J, Schneider U, Emrich HM. The pharmacology of psilocybin. <em>Addict Biol</em>. 2002;7(4):357&ndash;364. <a href="https://doi.org/10.1080/1355621021000005937">doi:10.1080/1355621021000005937</a></li>
            <li id="ref9">Studerus E, Kometer M, Hasler F, Vollenweider FX. Acute, subacute and long-term subjective effects of psilocybin in healthy humans: a pooled analysis of experimental studies. <em>J Psychopharmacol</em>. 2011;25(11):1434&ndash;1452. <a href="https://doi.org/10.1177/0269881110382466">doi:10.1177/0269881110382466</a></li>
            <li id="ref10">Griffiths RR, Richards WA, McCann U, Jesse R. Psilocybin can occasion mystical-type experiences having substantial and sustained personal meaning and spiritual significance. <em>Psychopharmacology</em>. 2006;187(3):268&ndash;283. <a href="https://doi.org/10.1007/s00213-006-0457-5">doi:10.1007/s00213-006-0457-5</a></li>
            <li id="ref11">Johnson MW, Sewell RA, Griffiths RR. Psilocybin dose-dependently causes delayed, transient headaches in healthy volunteers. <em>Drug Alcohol Depend</em>. 2012;123(1&ndash;3):132&ndash;140. <a href="https://doi.org/10.1016/j.drugalcdep.2011.10.029">doi:10.1016/j.drugalcdep.2011.10.029</a></li>
            <li id="ref12">Hinkle JT, Graziosi M, Nayak SM, Yaden DB. Adverse events in studies of classic psychedelics: a systematic review and meta-analysis. <em>JAMA Psychiatry</em>. 2024;81(12):1225&ndash;1235. <a href="https://doi.org/10.1001/jamapsychiatry.2024.2546">doi:10.1001/jamapsychiatry.2024.2546</a></li>
            <li id="ref13">Johnson MW, Richards WA, Griffiths RR. Human hallucinogen research: guidelines for safety. <em>J Psychopharmacol</em>. 2008;22(6):603&ndash;620. <a href="https://doi.org/10.1177/0269881108093587">doi:10.1177/0269881108093587</a></li>
            <li id="ref14">Schlag AK, Aday J, Salam I, Neill JC, Nutt DJ. Adverse effects of psychedelics: from anecdotes and misinformation to systematic science. <em>J Psychopharmacol</em>. 2022;36(3):258&ndash;272. <a href="https://doi.org/10.1177/02698811211069100">doi:10.1177/02698811211069100</a></li>
            <li id="ref15">Krebs TS, Johansen P&Oslash;. Psychedelics and mental health: a population study. <em>PLoS One</em>. 2013;8(8):e63972. <a href="https://doi.org/10.1371/journal.pone.0063972">doi:10.1371/journal.pone.0063972</a></li>
            <li id="ref16">Hendricks PS, Thorne CB, Clark CB, Coombs DW, Johnson MW. Classic psychedelic use is associated with reduced psychological distress and suicidality in the United States adult population. <em>J Psychopharmacol</em>. 2015;29(3):280&ndash;288. <a href="https://doi.org/10.1177/0269881114565653">doi:10.1177/0269881114565653</a></li>
            <li id="ref17">Halpern JH, Pope HG. Hallucinogen persisting perception disorder: what do we know after 50 years? <em>Drug Alcohol Depend</em>. 2003;69(2):109&ndash;119. <a href="https://doi.org/10.1016/S0376-8716(02)00306-X">doi:10.1016/S0376-8716(02)00306-X</a></li>
            <li id="ref18">Farah R, Kerns AF, Meyers AT, McCabe SE, et al. Psilocybin exposures reported to US poison centers: national trends over a decade. <em>J Adolesc Health</em>. 2024;74(5):1053&ndash;1056. <a href="https://doi.org/10.1016/j.jadohealth.2024.01.027">doi:10.1016/j.jadohealth.2024.01.027</a></li>
            <li id="ref19">Zendo Project (MAPS). Psychedelic harm reduction principles and peer-support manual. <a href="https://zendoproject.org/">zendoproject.org</a>; DanceSafe, Psilocybin mushroom drug information. <a href="https://dancesafe.org/">dancesafe.org</a></li>
            <li id="ref20">Nayak SM, Gukasyan N, Barrett FS, Erowid E, Erowid F, Griffiths RR. Classic psychedelic coadministration with lithium, but not lamotrigine, is associated with seizures: an analysis of online psychedelic experience reports. <em>Pharmacopsychiatry</em>. 2021;54(5):240&ndash;245. <a href="https://doi.org/10.1055/a-1524-2794">doi:10.1055/a-1524-2794</a></li>
            <li id="ref21">Sarparast A, Thomas K, Malcolm B, Stauffer CS. Drug-drug interactions between psychiatric medications and MDMA or psilocybin: a systematic review. <em>Psychopharmacology</em>. 2022;239(6):1945&ndash;1976. <a href="https://doi.org/10.1007/s00213-022-06083-y">doi:10.1007/s00213-022-06083-y</a></li>
            <li id="ref22">Carhart-Harris RL, Erritzoe D, Williams T, et al. Neural correlates of the psychedelic state as determined by fMRI studies with psilocybin. <em>Proc Natl Acad Sci USA</em>. 2012;109(6):2138&ndash;2143. <a href="https://doi.org/10.1073/pnas.1119598109">doi:10.1073/pnas.1119598109</a></li>
            <li id="ref23">Siegel JS, Subramanian S, Perry D, et al. Psilocybin desynchronizes the human brain. <em>Nature</em>. 2024;632:131&ndash;138. <a href="https://doi.org/10.1038/s41586-024-07624-5">doi:10.1038/s41586-024-07624-5</a></li>
            <li id="ref24">Shao LX, Liao C, Gregg I, et al. Psilocybin induces rapid and persistent growth of dendritic spines in frontal cortex in vivo. <em>Neuron</em>. 2021;109(16):2535&ndash;2544. <a href="https://doi.org/10.1016/j.neuron.2021.06.008">doi:10.1016/j.neuron.2021.06.008</a></li>
            <li id="ref25">Goodwin GM, Aaronson ST, Alvarez O, et al. Single-dose psilocybin for a treatment-resistant episode of major depression. <em>N Engl J Med</em>. 2022;387(18):1637&ndash;1648. <a href="https://doi.org/10.1056/NEJMoa2206443">doi:10.1056/NEJMoa2206443</a></li>
            <li id="ref26">Bogenschutz MP, Ross S, Bhatt S, et al. Percentage of heavy drinking days following psilocybin-assisted psychotherapy vs placebo in the treatment of adult patients with alcohol use disorder: a randomized clinical trial. <em>JAMA Psychiatry</em>. 2022;79(10):953&ndash;962. <a href="https://doi.org/10.1001/jamapsychiatry.2022.2096">doi:10.1001/jamapsychiatry.2022.2096</a></li>
        </ol>
        </div>
"""

ADDICTION_CONTENT = r"""        <h1 class="page-title">Os cogumelos viciam?</h1>
        <p class="page-subtitle">De WikiPsilocybin, a enciclopédia livre da psilocibina, um artigo de redução de danos</p>
        <p class="hatnote">Este artigo cobre a dependência e o potencial de abuso dos cogumelos de psilocibina. Sobre efeitos secundários, sobredosagem e segurança geral, veja <a href="/pt/are-magic-mushrooms-dangerous/">Os cogumelos mágicos são perigosos?</a></p>
        <div class="infobox">
            <div class="infobox-title">Potencial de abuso da psilocibina</div>
            <div class="infobox-row"><div class="infobox-label">Dependência física</div><div class="infobox-value">Não observada<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Síndrome de abstinência</div><div class="infobox-value">Nenhuma documentada<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Autoadministração em animais</div><div class="infobox-value">Fraca ou ausente; os animais não trabalham de forma fiável pela psilocibina<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref3">[3]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Tolerância</div><div class="infobox-value">Desenvolve-se em dias; restabelece-se em grande medida após 1&ndash;2 semanas<sup class="ref"><a href="#ref4">[4]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Recomendação pericial de classificação</div><div class="infobox-value">Lista IV (baixo potencial de abuso) se aprovada medicamente<sup class="ref"><a href="#ref1">[1]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Classificação atual nos EUA</div><div class="infobox-value">Lista I</div></div>
        </div>
        <p><strong>Os cogumelos de psilocibina («cogumelos» ou «shrooms») não se consideram viciantes do modo em que o são o álcool, a nicotina, os opioides ou os estimulantes.</strong> Não produzem dependência física nem uma síndrome de abstinência, os animais de laboratório não os autoadministram de forma fiável, e a tolerância rápida que produzem faz com que o uso diário se limite por si.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref4">[4]</a></sup> Uma revisão exaustiva da psilocibina face aos oito fatores de potencial de abuso da Controlled Substances Act dos EUA concluiu que, se se aprovasse como medicamento, encaixaria na Lista IV, a categoria de drogas com baixo potencial de abuso como as benzodiazepinas e o zolpidem, e não na Lista I onde se situa agora.<sup class="ref"><a href="#ref1">[1]</a></sup></p>
        <p>Isso não significa que o uso problemático seja impossível. Uma minoria de pessoas usa alucinogénios de forma bastante compulsiva para cumprir critérios de <em>transtorno por uso de alucinogénios</em>, um diagnóstico do DSM-5, e podem formar-se hábitos psicológicos em torno de qualquer experiência que uma pessoa encontre significativa ou evasiva.<sup class="ref"><a href="#ref5">[5]</a></sup> Este artigo explica a distinção, o que diz a evidência e o pequeno número de situações em que o uso de cogumelos merece atenção.</p>
        <div class="toc">
            <div class="toc-title">Conteúdo</div>
            <ol>
                <li><a href="#short-answer">A resposta breve</a></li>
                <li><a href="#what-addiction-means">O que significa «viciante»</a></li>
                <li><a href="#evidence">A evidência</a></li>
                <li><a href="#tolerance">A tolerância e porque importa</a></li>
                <li><a href="#withdrawal">Abstinência</a></li>
                <li><a href="#use-disorder">Transtorno por uso de alucinogénios</a></li>
                <li><a href="#microdosing">A microdose muda o panorama?</a></li>
                <li><a href="#treatment">A psilocibina como tratamento da dependência</a></li>
                <li><a href="#harm-reduction">Redução de danos</a></li>
                <li><a href="#references">Referências</a></li>
            </ol>
        </div>
        <h2 id="short-answer">A resposta breve</h2>
        <p>Não, segundo as definições científicas habituais. O National Institute on Drug Abuse dos EUA afirma que não se sabe que a psilocibina cause dependência física, e a própria ficha da Drug Enforcement Administration assinala que a psilocibina não produz conduta compulsiva de procura da droga em modelos animais.<sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref6">[6]</a></sup> Na análise multicritério de dano da <em>Lancet</em> de 2010, os cogumelos de psilocibina obtiveram a pontuação mais baixa de 20 drogas no critério de «dependência» e também no dano global.<sup class="ref"><a href="#ref7">[7]</a></sup></p>
        <p>Os traços que tornam uma droga viciante, isto é, uma ativação forte da via de recompensa dopaminérgica do cérebro, um uso crescente, abstinência física e ânsia entre usos, são fracos ou estão ausentes na psilocibina. A maioria das pessoas que experimenta cogumelos usa-os um punhado de vezes na vida; a National Survey on Drug Use and Health encontra de forma consistente que o uso no mês anterior é uma fração pequena do uso ao longo da vida, um padrão oposto ao das drogas viciantes.<sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <h2 id="what-addiction-means">O que significa «viciante»</h2>
        <p>Quem pesquisa a dependência distingue várias coisas a que «viciante» pode referir-se:</p>
        <ul>
            <li><strong>Dependência física</strong>: o corpo adapta-se à droga de modo que deixá-la causa uma síndrome de abstinência (álcool, opioides, benzodiazepinas).</li>
            <li><strong>Reforço</strong>: a droga ativa de forma direta os circuitos de recompensa de modo que animais e pessoas trabalharão para a obter de forma repetida (cocaína, nicotina).</li>
            <li><strong>Uso compulsivo</strong>: uso continuado apesar do dano, perda de controlo, ânsia; este é o núcleo de um transtorno por uso de substâncias do DSM-5.</li>
            <li><strong>Hábito psicológico</strong>: dependência de uma experiência para enfrentar ou evadir-se, que pode aderir a quase qualquer atividade.</li>
        </ul>
        <p>A psilocibina pontua baixo nos três primeiros e, como qualquer experiência potente, não é imune ao quarto.</p>
        <h2 id="evidence">A evidência</h2>
        <h3>Estudos em animais</h3>
        <p>O teste de laboratório habitual de potencial de abuso é se os animais se autoadministrarão uma droga. Os ratos e os macacos autoadministram com facilidade cocaína, heroína, nicotina e álcool. Os psicadélicos clássicos, incluída a psilocibina, estão entre as poucas drogas psicoativas que os animais não se autoadministram de forma fiável, e nos testes de preferência de lugar condicionada produzem preferência fraca ou nula.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref3">[3]</a></sup> A psilocina também não aumenta de forma substancial a dopamina no núcleo accumbens, a assinatura das drogas reforçantes, embora tenha efeitos dopaminérgicos indiretos modestos.<sup class="ref"><a href="#ref3">[3]</a></sup></p>
        <h3>Estudos clínicos e de laboratório em humanos</h3>
        <p>Em mais de duas décadas de ensaios clínicos modernos com mais de mil pessoas participantes que receberam psilocibina sob supervisão, nenhum estudo comunicou procura da droga, ânsia ou uso compulsivo posterior como desfecho.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref9">[9]</a></sup> Uma metanálise de 2024 de eventos adversos em ensaios de psicadélicos clássicos não encontrou casos de dependência.<sup class="ref"><a href="#ref9">[9]</a></sup> O seguimento de pessoas voluntárias saudáveis nos estudos de Johns Hopkins concluiu que a alteração mais habitual no uso de drogas após uma sessão de dose alta foi uma <em>descida</em> do uso de outras substâncias.<sup class="ref"><a href="#ref10">[10]</a></sup></p>
        <h3>Dados populacionais</h3>
        <p>Entre os adultos dos EUA, o uso de psilocibina ao longo da vida é habitual (cerca de um em cada dez), mas o uso regular é raro. As análises da National Survey on Drug Use and Health não encontraram associação entre o uso de psicadélicos ao longo da vida e um aumento dos problemas de saúde mental, e algumas análises encontraram que o uso de psicadélicos se associava a menores probabilidades de transtorno por uso de opioides.<sup class="ref"><a href="#ref8">[8]</a></sup><sup class="ref"><a href="#ref11">[11]</a></sup></p>
        <h2 id="tolerance">A tolerância e porque importa</h2>
        <p>A psilocibina produz uma tolerância rápida e pronunciada. Tomar uma segunda dose em um ou dois dias produz um efeito marcadamente mais fraco, e a dosagem diária durante uns poucos dias pode abolir o efeito psicadélico quase por completo; a sensibilidade volta após aproximadamente uma ou duas semanas de abstinência.<sup class="ref"><a href="#ref4">[4]</a></sup> Isto deve-se à regulação em baixa dos recetores 5-HT<sub>2A</sub> sobre os quais atua a psilocina, e aplica-se de forma cruzada ao LSD e à mescalina.<sup class="ref"><a href="#ref4">[4]</a></sup></p>
        <p>A tolerância rápida é uma das principais razões farmacológicas pelas quais a psilocibina é difícil de usar de forma compulsiva: o uso diário crescente simplesmente deixa de funcionar. Contrasta de forma nítida com drogas como os opioides, em que a tolerância impulsiona doses mais altas em vez de retirar o incentivo a voltar a dosar.</p>
        <h2 id="withdrawal">Abstinência</h2>
        <p>Não se documentou uma síndrome de abstinência física para a psilocibina em humanos nem em animais, e não figura entre as substâncias com uma síndrome de abstinência reconhecida no DSM-5.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup> Quem deixa de usá-la após um período de uso frequente pode notar um «baixo» de fadiga, ânimo baixo ou aplanamento durante um ou dois dias após sessões individuais, mas isto é um efeito posterior da experiência mais do que uma síndrome de dependência, e não impulsiona a voltar a dosar.<sup class="ref"><a href="#ref12">[12]</a></sup></p>
        <h2 id="use-disorder">Transtorno por uso de alucinogénios</h2>
        <p>O DSM-5 inclui o «transtorno por uso de outros alucinogénios» (distinto da fenciclidina), que pode diagnosticar-se quando uma pessoa mostra um padrão problemático de uso, por exemplo dedicar tempo excessivo a obter ou usar, abandonar atividades importantes ou continuar apesar do dano.<sup class="ref"><a href="#ref5">[5]</a></sup> Como a tolerância conta como um critério e a abstinência não se aplica, o diagnóstico apoia-se sobretudo em critérios comportamentais. A prevalência é baixa: o DSM-5 cita uma prevalência a 12 meses de cerca de 0.1% entre os adultos dos EUA, e nas populações que procuram tratamento os alucinogénios raramente são a droga principal.<sup class="ref"><a href="#ref5">[5]</a></sup><sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <p>Os sinais de alerta de que o uso se tornou problemático assemelham-se aos de qualquer substância: usar com mais frequência do que a prevista, usar para evitar enfrentar a vida mais do que para comprometer-se com ela, um uso que interfere com o trabalho, as relações ou a segurança, e dificuldade para parar apesar de querer fazê-lo. Como a psilocibina não produz dependência física, a resposta adequada é o apoio psicológico mais do que a desintoxicação médica. A National Helpline da SAMHSA (1-800-662-4357) oferece encaminhamentos gratuitos e confidenciais.<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <h2 id="microdosing">A microdose muda o panorama?</h2>
        <p>A microdose, tomar quantidades subpercetuais a cada poucos dias, é o único padrão de uso de psilocibina que é habitual por desenho. Mesmo aqui, não se observou dependência no sentido farmacológico, e a maioria dos protocolos inclui dias de descanso precisamente pela tolerância.<sup class="ref"><a href="#ref14">[14]</a></sup> As perguntas em aberto com a microdose concernem à eficácia (os estudos controlados com placebo mostram que a maioria dos benefícios comunicados é igualada pelo placebo) e à falta de dados de segurança a longo prazo sobre a ativação repetida dos recetores 5-HT<sub>2B</sub>, uma preocupação teórica de válvula cardíaca, mais do que à dependência.<sup class="ref"><a href="#ref14">[14]</a></sup><sup class="ref"><a href="#ref15">[15]</a></sup></p>
        <h2 id="treatment">A psilocibina como tratamento da dependência</h2>
        <p>Em vez de causar dependência, a psilocibina estuda-se como tratamento dela. Num ensaio aleatorizado de 2022 na NYU, duas sessões supervisionadas de psilocibina combinadas com terapia reduziram os dias de consumo intenso de álcool em pessoas com transtorno por uso de álcool em 83% ao longo de oito meses, face a 51% com um placebo ativo.<sup class="ref"><a href="#ref16">[16]</a></sup> Um estudo-piloto de Johns Hopkins de psilocibina para a cessação do tabaco comunicou 80% de abstinência verificada biologicamente aos seis meses e 60% aos 30 meses, muito acima das taxas dos tratamentos convencionais, embora o estudo fosse pequeno e não controlado.<sup class="ref"><a href="#ref17">[17]</a></sup> Há em marcha ensaios maiores em transtornos por uso de álcool, tabaco, opioides e cocaína.</p>
        <h2 id="harm-reduction">Redução de danos</h2>
        <p>Como o risco de dependência é baixo, a redução de danos para os cogumelos centra-se nos riscos agudos cobertos em <a href="/pt/are-magic-mushrooms-dangerous/">Os cogumelos mágicos são perigosos?</a>: identificação de cogumelos, dose, ambiente, um acompanhante sóbrio e evitar combinações com lítio, álcool e estimulantes. Específico dos padrões de uso:</p>
        <ul>
            <li><strong>Separe as sessões.</strong> A tolerância significa que voltar a dosar em questão de dias se desperdiça em grande medida e acrescenta esforço físico sem efeito. Muitas pessoas utilizadoras experientes e clínicas sugerem semanas ou meses entre doses completas.</li>
            <li><strong>Note o motivo.</strong> Usar para explorar, celebrar ou processar é distinto de usar para evitar. Se os cogumelos se tornaram o modo de enfrentar algo, esse algo continua a necessitar de atenção.</li>
            <li><strong>Vigie outras substâncias.</strong> As pessoas que desenvolvem problemas em torno dos psicadélicos têm com frequência um uso problemático concomitante de álcool ou cannabis; essas costumam ser as drogas que há que abordar primeiro.</li>
            <li><strong>Os antecedentes de saúde mental importam mais do que o risco de dependência.</strong> A razão principal para ser cauteloso com o uso repetido é a vulnerabilidade psiquiátrica, não a dependência.</li>
        </ul>
        <h2 id="see-also">Ver também</h2>
        <div class="see-also">
        <ul>
            <li><a href="/pt/are-magic-mushrooms-dangerous/">Os cogumelos mágicos são perigosos?</a>: efeitos secundários, más viagens, sobredosagem e interações medicamentosas</li>
            <li><a href="/pt/">Psilocibina</a>: panorama, farmacologia, pesquisa e situação legal</li>
            <li><a href="/pt/#therapeutic">Aplicações terapêuticas</a>: ensaios em transtornos por uso de substâncias</li>
        </ul>
        </div>
<div class="ambox help">
            <strong>Se alguém precisa de ajuda agora mesmo:</strong> US Poison Control <strong>1-800-222-1222</strong> (24/7, gratuito, confidencial) &middot; Emergências <strong>911</strong> &middot; SAMHSA National Helpline <strong>1-800-662-4357</strong> &middot; Linha de apoio entre pares psicadélico de Fireside Project <strong>62-FIRESIDE (623-473-7433)</strong> &middot; 988 Suicide &amp; Crisis Lifeline: ligue ou envie uma mensagem de texto para o <strong>988</strong>.
        </div>
        <h2 id="references">Referências</h2>
        <div class="refs">
        <ol>
            <li id="ref1">Johnson MW, Griffiths RR, Hendricks PS, Henningfield JE. The abuse potential of medical psilocybin according to the 8 factors of the Controlled Substances Act. <em>Neuropharmacology</em>. 2018;142:143&ndash;166. <a href="https://doi.org/10.1016/j.neuropharm.2018.05.012">doi:10.1016/j.neuropharm.2018.05.012</a></li>
            <li id="ref2">National Institute on Drug Abuse. Psilocybin (magic mushrooms). NIDA drug facts. <a href="https://nida.nih.gov/research-topics/psilocybin-magic-mushrooms">nida.nih.gov</a></li>
            <li id="ref3">Nichols DE. Psychedelics. <em>Pharmacol Rev</em>. 2016;68(2):264&ndash;355. <a href="https://doi.org/10.1124/pr.115.011478">doi:10.1124/pr.115.011478</a></li>
            <li id="ref4">Passie T, Seifert J, Schneider U, Emrich HM. The pharmacology of psilocybin. <em>Addict Biol</em>. 2002;7(4):357&ndash;364. <a href="https://doi.org/10.1080/1355621021000005937">doi:10.1080/1355621021000005937</a></li>
            <li id="ref5">American Psychiatric Association. <em>Diagnostic and Statistical Manual of Mental Disorders</em>, 5th ed., text revision (DSM-5-TR). 2022. Section: Other Hallucinogen Use Disorder.</li>
            <li id="ref6">US Drug Enforcement Administration. Psilocybin drug fact sheet. <a href="https://www.dea.gov/factsheets/psilocybin">dea.gov/factsheets/psilocybin</a></li>
            <li id="ref7">Nutt DJ, King LA, Phillips LD. Drug harms in the UK: a multicriteria decision analysis. <em>Lancet</em>. 2010;376(9752):1558&ndash;1565. <a href="https://doi.org/10.1016/S0140-6736(10)61462-6">doi:10.1016/S0140-6736(10)61462-6</a></li>
            <li id="ref8">Substance Abuse and Mental Health Services Administration. Key substance use and mental health indicators in the United States: results from the National Survey on Drug Use and Health. Annual reports. <a href="https://www.samhsa.gov/data/">samhsa.gov/data</a></li>
            <li id="ref9">Hinkle JT, Graziosi M, Nayak SM, Yaden DB. Adverse events in studies of classic psychedelics: a systematic review and meta-analysis. <em>JAMA Psychiatry</em>. 2024;81(12):1225&ndash;1235. <a href="https://doi.org/10.1001/jamapsychiatry.2024.2546">doi:10.1001/jamapsychiatry.2024.2546</a></li>
            <li id="ref10">Griffiths RR, Johnson MW, Richards WA, et al. Psilocybin occasioned mystical-type experiences: immediate and persisting dose-related effects. <em>Psychopharmacology</em>. 2011;218(4):649&ndash;665. <a href="https://doi.org/10.1007/s00213-011-2358-5">doi:10.1007/s00213-011-2358-5</a></li>
            <li id="ref11">Jones G, Ricard JA, Lipson J, Nock MK. Associations between classic psychedelics and opioid use disorder in a nationally-representative U.S. adult sample. <em>Sci Rep</em>. 2022;12:4099. <a href="https://doi.org/10.1038/s41598-022-08085-4">doi:10.1038/s41598-022-08085-4</a></li>
            <li id="ref12">Studerus E, Kometer M, Hasler F, Vollenweider FX. Acute, subacute and long-term subjective effects of psilocybin in healthy humans: a pooled analysis of experimental studies. <em>J Psychopharmacol</em>. 2011;25(11):1434&ndash;1452. <a href="https://doi.org/10.1177/0269881110382466">doi:10.1177/0269881110382466</a></li>
            <li id="ref13">Substance Abuse and Mental Health Services Administration. National Helpline, 1-800-662-HELP (4357). <a href="https://www.samhsa.gov/find-help/national-helpline">samhsa.gov/find-help/national-helpline</a></li>
            <li id="ref14">Szigeti B, Kartner L, Blemings A, et al. Self-blinding citizen science to explore psychedelic microdosing. <em>eLife</em>. 2021;10:e62878. <a href="https://doi.org/10.7554/eLife.62878">doi:10.7554/eLife.62878</a></li>
            <li id="ref15">Kuypers KPC, Ng L, Erritzoe D, et al. Microdosing psychedelics: more questions than answers? An overview and suggestions for future research. <em>J Psychopharmacol</em>. 2019;33(9):1039&ndash;1057. <a href="https://doi.org/10.1177/0269881119857204">doi:10.1177/0269881119857204</a></li>
            <li id="ref16">Bogenschutz MP, Ross S, Bhatt S, et al. Percentage of heavy drinking days following psilocybin-assisted psychotherapy vs placebo in the treatment of adult patients with alcohol use disorder: a randomized clinical trial. <em>JAMA Psychiatry</em>. 2022;79(10):953&ndash;962. <a href="https://doi.org/10.1001/jamapsychiatry.2022.2096">doi:10.1001/jamapsychiatry.2022.2096</a></li>
            <li id="ref17">Johnson MW, Garcia-Romeu A, Griffiths RR. Long-term follow-up of psilocybin-facilitated smoking cessation. <em>Am J Drug Alcohol Abuse</em>. 2017;43(1):55&ndash;60. <a href="https://doi.org/10.3109/00952990.2016.1170135">doi:10.3109/00952990.2016.1170135</a></li>
        </ol>
        </div>
"""


def main() -> None:
    pages = [
        {
            "page": "/",
            "title": "Psilocibina | WikiPsilocybin",
            "description": "WikiPsilocybin é uma enciclopédia independente de pesquisa sobre psilocibina, ensaios clínicos, notícias legais e redução de danos. Cada afirmação está citada a uma fonte primária.",
            "content": HOME_CONTENT,
            "extra_nav": True,
        },
        {
            "page": "/are-magic-mushrooms-dangerous/",
            "title": "Os cogumelos mágicos são perigosos? Riscos, efeitos secundários e segurança | WikiPsilocybin",
            "description": "Os cogumelos mágicos são perigosos? Uma revisão baseada em evidência dos riscos da psilocibina: efeitos secundários, más viagens, sobredosagem e sintomas de envenenamento, interações medicamentosas, contraindicações de saúde mental e redução de danos. Completamente referenciada.",
            "content": DANGER_CONTENT,
            "extra_nav": False,
        },
        {
            "page": "/are-shrooms-addictive/",
            "title": "Os cogumelos viciam? Dependência, tolerância e abstinência | WikiPsilocybin",
            "description": "Os cogumelos viciam? O que diz a pesquisa sobre a dependência da psilocibina, a tolerância, a abstinência e o transtorno por uso de alucinogénios, e porque os especialistas classificam o seu potencial de abuso como baixo. Completamente referenciada.",
            "content": ADDICTION_CONTENT,
            "extra_nav": False,
        },
    ]
    for spec in pages:
        html = render_page(
            lang="pt",
            page=spec["page"],
            title=spec["title"],
            description=spec["description"],
            content=spec["content"],
            active_tab="article",
            extra_nav=spec["extra_nav"],
        )
        dest = write_page("pt", spec["page"], html)
        print(f"wrote {dest}")


if __name__ == "__main__":
    main()
