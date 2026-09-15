#!/usr/bin/env python3
"""Write Spanish translations of the homepage and two safety guides."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from i18n_chrome import render_page, write_page

HOME_CONTENT = r"""        <h1 class="page-title">Psilocibina</h1>
        <p class="page-subtitle">De WikiPsilocybin, la enciclopedia libre de la psilocibina, actualizada a diario</p>

        <div class="infobox">
            <div class="infobox-title">Psilocibina</div>
            <div class="infobox-image">
                <img src="https://d8j0ntlcm91z4.cloudfront.net/user_36uL1HV6CQZ9Ia0ikUE78jQJB98/hf_20260808_070842_c807ec80-0269-48c6-a459-06b22fa82a97.png" alt="Visualización molecular de la psilocibina">
                <div class="caption">Ilustración de la conectividad de una red neuronal (representación artística, no es una imagen de investigación)</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Fórmula</div>
                <div class="infobox-value">C&#8321;&#8322;H&#8321;&#8327;N&#8322;O&#8324;P</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Masa molar</div>
                <div class="infobox-value">284.25 g/mol</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Primer aislamiento</div>
                <div class="infobox-value">1958, por Albert Hofmann</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Especies conocidas</div>
                <div class="infobox-value">más de 200 hongos</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Ensayos clínicos</div>
                <div class="infobox-value">más de 400 registrados</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Uso humano</div>
                <div class="infobox-value">~6.000 años documentados</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Situación legal</div>
                <div class="infobox-value">Varía; Lista I (federal de EE. UU.), uso terapéutico legal en OR, CO, AU</div>
            </div>
        </div>

        <div id="recent-events" class="recent-events">
            <h3>Acontecimientos recientes</h3>
            <ul class="event-list">
                <li>
                    <span class="event-date">6 ago 2026</span>
                    <span class="event-tag tag-policy">Política</span>
                    <span class="event-link"><a href="/events/2026-08-06-va-pivot-trial/">VA launches PIVOT, a five-site randomized trial of psilocybin for veterans with treatment-resistant depression</a></span>
                </li>
                <li>
                    <span class="event-date">30 jul 2026</span>
                    <span class="event-tag tag-research">Investigación</span>
                    <span class="event-link"><a href="/events/2026-07-30-osu-veterans-ptsd-pilot/">Ohio State pilot trial: 9 of 12 veterans with severe, treatment-resistant PTSD in remission one month after psilocybin-assisted therapy</a></span>
                </li>
                <li>
                    <span class="event-date">26 ene 2026</span>
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
                    <span class="event-tag tag-research">Investigación</span>
                    <span class="event-link"><a href="/events/2024-07-17-washu-psilocybin-desynchronizes-brain/">Washington University study in Nature shows psilocybin desynchronizes the brain's default mode network, with some changes lasting weeks</a></span>
                </li>
            </ul>
            <span class="view-all-link"><a href="/es/events/">Ver todos los acontecimientos &rarr;</a></span>
        </div>

        <div class="toc">
            <div class="toc-title">Contenido</div>
            <ol>
                <li><a href="#what-is">¿Qué es la psilocibina?</a></li>
                <li><a href="#how-it-works">Cómo actúa</a></li>
                <li><a href="#research">Investigación y ensayos clínicos</a></li>
                <li><a href="#therapeutic">Aplicaciones terapéuticas</a></li>
                <li><a href="#microdosing">Microdosis</a></li>
                <li><a href="#legal">Situación legal</a></li>
                <li><a href="#safety">Seguridad y reducción de daños</a></li>
            </ol>
        </div>

        <h2 id="what-is">¿Qué es la psilocibina?</h2>
        <p>La psilocibina es un compuesto psicodélico de origen natural producido por más de 200 especies de hongos, conocidos habitualmente como «hongos mágicos». Tras su ingestión, el cuerpo convierte la psilocibina en psilocina, que interactúa con los receptores de serotonina del cerebro y produce estados alterados de conciencia, cambios visuales y auditivos, y transformaciones profundas de la percepción y el pensamiento.</p>
        <p>Aislada y sintetizada por primera vez por el químico suizo Albert Hofmann en 1958, la psilocibina se ha usado en prácticas ceremoniales indígenas durante miles de años. La evidencia arqueológica sugiere un uso humano de hongos con psilocibina que se remonta al menos a 6.000 años en las culturas mesoamericanas.</p>

        <h2 id="how-it-works">Cómo actúa</h2>
        <p>La psilocibina es un profármaco: biológicamente inactiva hasta que el cuerpo la metaboliza. Tras la ingestión, las enzimas fosfatasa alcalina del intestino y el hígado eliminan un grupo fosfato y convierten la psilocibina en psilocina (4-hidroxi-N,N-dimetiltriptamina).</p>
        <p>El principal mecanismo de acción de la psilocina es el agonismo de los receptores de serotonina 5-HT<sub>2A</sub> en la corteza prefrontal. Esto desencadena una cascada de efectos:</p>
        <ul>
            <li><strong>Interrupción de la red neuronal por defecto (DMN)</strong>: reduce la actividad del sistema de «piloto automático» del cerebro y permite que se formen conexiones neuronales nuevas</li>
            <li><strong>Mayor conectividad neuronal</strong>: regiones cerebrales que habitualmente no se comunican empiezan a interactuar y producen experiencias sinestésicas y asociativas</li>
            <li><strong>Promoción de la neuroplasticidad</strong>: estimula el crecimiento dendrítico y la densidad sináptica, en particular en la corteza prefrontal y el hipocampo</li>
            <li><strong>Procesamiento emocional</strong>: aumenta la respuesta de la amígdala a estímulos emocionales y reduce la reactividad basada en el miedo</li>
        </ul>
        <div class="ambox">
            <strong>Duración de los efectos:</strong> El inicio suele ocurrir 20&ndash;40 minutos después de la ingestión. Los efectos máximos duran 2&ndash;3 horas, con una duración total de 4&ndash;6 horas. Los efectos residuales sobre el ánimo y la cognición pueden persistir días o semanas.
        </div>

        <h2 id="research">Investigación y ensayos clínicos</h2>
        <p>La última década ha visto un resurgimiento sin precedentes de la investigación sobre psilocibina, con instituciones importantes como Johns Hopkins, Imperial College London, NYU y Yale que llevan a cabo ensayos clínicos rigurosos.</p>

        <h3>Hitos clave de la investigación</h3>
        <ul>
            <li><strong>2016:</strong> Johns Hopkins y NYU publican simultáneamente estudios de referencia que muestran que la psilocibina produce descensos sustanciales y sostenidos de la ansiedad y la depresión en pacientes con cáncer</li>
            <li><strong>2020:</strong> Se establece el Johns Hopkins Center for Psychedelic &amp; Consciousness Research con 17 millones de dólares de financiación</li>
            <li><strong>2021:</strong> JAMA Psychiatry publica un ensayo aleatorizado que muestra que la terapia con psilocibina es al menos tan eficaz como el escitalopram (Lexapro) para el trastorno depresivo mayor</li>
            <li><strong>2023:</strong> La FDA concede la designación Breakthrough Therapy a la terapia asistida con psilocibina para la depresión resistente al tratamiento</li>
            <li><strong>2024&ndash;2026:</strong> Múltiples ensayos clínicos de fase 3 en curso o completados para depresión, TEPT, adicción y malestar al final de la vida</li>
        </ul>
        <div class="ambox">
            <strong>Recuento actual de ensayos:</strong> A fecha de 2026, hay más de 400 ensayos clínicos registrados que involucran psilocibina listados en ClinicalTrials.gov, que abarcan indicaciones desde la depresión mayor hasta la anorexia, las cefaleas en racimos y el trastorno por uso de opioides.
        </div>

        <h2 id="therapeutic">Aplicaciones terapéuticas</h2>
        <p>La terapia asistida con psilocibina combina los efectos farmacológicos de la psilocibina con un apoyo psicoterapéutico estructurado. La evidencia actual respalda su potencial para tratar:</p>
        <ul>
            <li><strong>Trastorno depresivo mayor (MDD)</strong>: tasas de respuesta del 60&ndash;80% en ensayos clínicos, con efectos que duran 3&ndash;12 meses después de 1&ndash;2 sesiones</li>
            <li><strong>Depresión resistente al tratamiento (TRD)</strong>: designación Breakthrough Therapy de la FDA concedida; ensayos de fase 3 en curso</li>
            <li><strong>Malestar al final de la vida</strong>: reduce la ansiedad existencial y la depresión en pacientes con cáncer terminal</li>
            <li><strong>TEPT</strong>: evidencia emergente de estudios centrados en veteranos muestra una reducción significativa de los síntomas</li>
            <li><strong>Trastornos por uso de sustancias</strong>: resultados prometedores para el cese del tabaco y el alcohol, con tasas de abandono 2&ndash;3 veces superiores a las de los tratamientos convencionales</li>
            <li><strong>Cefaleas en racimos</strong>: alivio comunicado por pacientes y apoyo clínico creciente</li>
        </ul>

        <h2 id="microdosing">Microdosis</h2>
        <p>La microdosis consiste en tomar dosis subperceptuales de psilocibina: habitualmente 50&ndash;200 mg de material de hongo seco, o aproximadamente 1/10 a 1/20 de una dosis completa. Quienes lo practican comunican mejoras en la creatividad, la concentración, la regulación emocional y el bienestar general sin experimentar efectos psicodélicos.</p>
        <p>Aunque la evidencia anecdótica es abundante, la investigación controlada sobre microdosis sigue siendo limitada. Entre los estudios destacados se incluyen:</p>
        <ul>
            <li>El estudio de autocegamiento de 2022 de The Beckley Foundation, que encontró que algunos beneficios persistían incluso en el grupo placebo, lo que sugiere que los efectos de expectativa desempeñan un papel</li>
            <li>El estudio de 2023 de la University of British Columbia que mostró que quienes tomaban microdosis comunicaban mejor ánimo y menos ansiedad que quienes no las tomaban</li>
            <li>Ensayos en curso financiados por el NIH que evalúan protocolos estandarizados de microdosis para el refuerzo cognitivo y los trastornos del ánimo</li>
        </ul>

        <h2 id="legal">Situación legal</h2>
        <p>El panorama legal de la psilocibina evoluciona con rapidez en todo el mundo:</p>
        <h3>Estados Unidos</h3>
        <ul>
            <li><strong>Oregón</strong>: primer estado en legalizar la terapia regulada con psilocibina (Measure 109, 2020), con centros de servicio con licencia en funcionamiento desde 2023</li>
            <li><strong>Colorado</strong>: la Proposition 122 (2022) despenalizó la psilocibina y creó un marco de acceso regulado para uso terapéutico</li>
            <li><strong>Despenalización municipal</strong>: ciudades como Denver, Oakland, Santa Cruz, Seattle, Detroit y otras han restado prioridad a la aplicación de la ley</li>
            <li><strong>Federal</strong>: la psilocibina sigue en la Lista I de la Controlled Substances Act, aunque la legislación bipartidista para exenciones de investigación sigue avanzando</li>
        </ul>

        <h3>Internacional</h3>
        <ul>
            <li><strong>Canadá</strong>: el Special Access Program permite a los profesionales sanitarios solicitar psilocibina para afecciones resistentes al tratamiento</li>
            <li><strong>Australia</strong>: la TGA aprobó la psilocibina para la depresión resistente al tratamiento en entornos de psiquiatras autorizados (julio de 2023)</li>
            <li><strong>Jamaica y Países Bajos</strong>: trufas/hongos de psilocibina disponibles a través de zonas grises legales o de legalidad explícita</li>
            <li><strong>Unión Europea</strong>: varios países exploran marcos regulatorios; los ensayos clínicos se expanden en Alemania, el Reino Unido y Suiza</li>
        </ul>

        <h2 id="safety">Seguridad y reducción de daños</h2>
        <p class="hatnote">Artículos principales: <a href="/es/are-magic-mushrooms-dangerous/">¿Son peligrosos los hongos mágicos?</a> y <a href="/es/are-shrooms-addictive/">¿Crean adicción los hongos?</a></p>
        <p>La psilocibina tiene un perfil de seguridad bien establecido en comparación con otras sustancias psicoactivas. Su dosis letal estimada es aproximadamente 1.000 veces una dosis eficaz típica, no se ha documentado de forma fiable ninguna sobredosis mortal por psilocibina sola en un adulto sano, no produce dependencia física ni abstinencia, y la tolerancia rápida desalienta el uso frecuente. El análisis multicriterio de 2010 en <em>Lancet</em> de David Nutt y colegas clasificó los hongos de psilocibina como los menos dañinos de 20 drogas recreativas al considerar tanto el daño a los usuarios como el daño a terceros.</p>
        <p>Los riesgos que sí existen son sobre todo psicológicos y situacionales, más que tóxicos:</p>
        <ul>
            <li><strong>Malos viajes</strong>: ansiedad aguda, pánico o confusión; en una encuesta de casi 2.000 experiencias difíciles, el 11% de las personas encuestadas se pusieron a sí mismas o a otras en riesgo físico y el 7.6% buscó después tratamiento por síntomas persistentes</li>
            <li><strong>Vulnerabilidad psiquiátrica</strong>: no se recomienda a personas con antecedentes personales o familiares de trastornos psicóticos o bipolar I</li>
            <li><strong>Interacciones farmacológicas</strong>: el litio se asocia con convulsiones cuando se combina con psicodélicos; los ISRS atenúan los efectos; los IMAO pueden intensificarlos</li>
            <li><strong>Cardiovascular</strong>: aumentos moderados y transitorios de la frecuencia cardíaca y la presión arterial; precaución con enfermedad cardíaca preexistente</li>
            <li><strong>Identificación errónea</strong>: especies mortales de <em>Amanita</em> y <em>Galerina</em> pueden parecerse a los hongos de psilocibina; los hongos recolectados son la principal fuente de envenenamientos mortales por «hongos mágicos»</li>
            <li><strong>Set y setting</strong>: un acompañante sobrio, un entorno privado seguro y una dosis conservadora son las salvaguardas más eficaces</li>
        </ul>
        <div class="ambox">
            <strong>¿Necesitas ayuda ahora?</strong> US Poison Control 1-800-222-1222 (gratuito, confidencial, 24/7) &middot; Fireside Project apoyo entre pares psicodélico 62-FIRESIDE (623-473-7433) &middot; 988 Suicide &amp; Crisis Lifeline. Para el detalle completo y las referencias, véase <a href="/es/are-magic-mushrooms-dangerous/">¿Son peligrosos los hongos mágicos?</a>
        </div>
"""

DANGER_CONTENT = r"""        <h1 class="page-title">¿Son peligrosos los hongos mágicos?</h1>
        <p class="page-subtitle">De WikiPsilocybin, la enciclopedia libre de la psilocibina, un artículo de reducción de daños</p>
        <p class="hatnote">Este artículo cubre los riesgos, los efectos secundarios y la seguridad de los hongos de psilocibina («hongos» o «shrooms»). Sobre el compuesto en sí, véase <a href="/es/">Psilocibina</a>. Sobre dependencia y potencial de abuso, véase <a href="/es/are-shrooms-addictive/">¿Crean adicción los hongos?</a></p>
        <div class="infobox">
            <div class="infobox-title">Seguridad de los hongos de psilocibina</div>
            <div class="infobox-row"><div class="infobox-label">Toxicidad física</div><div class="infobox-value">Muy baja; la proporción dosis letal/dosis eficaz se estima cerca de 1,000:1<sup class="ref"><a href="#ref3">[3]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Muertes confirmadas por psilocibina sola</div><div class="infobox-value">Prácticamente ninguna en la literatura; las muertes implican hongos tóxicos mal identificados, accidentes o drogas coingeridas<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Principales riesgos</div><div class="infobox-value">Malestar psicológico («mal viaje»), conducta de riesgo bajo los efectos, psicosis en personas vulnerables, interacciones farmacológicas, identificación errónea de hongos</div></div>
            <div class="infobox-row"><div class="infobox-label">Clasificación global de daño</div><div class="infobox-value">La más baja de 20 drogas en el análisis multicriterio de <em>Lancet</em> de 2010<sup class="ref"><a href="#ref1">[1]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Poison Control (EE. UU.)</div><div class="infobox-value">1-800-222-1222</div></div>
        </div>
        <p><strong>Los hongos mágicos están entre las drogas recreativas físicamente menos peligrosas que se han estudiado, pero no están exentos de riesgo.</strong> Los peligros principales son psicológicos más que toxicológicos: experiencias aterradoras o desestabilizadoras, accidentes bajo los efectos y el desencadenamiento de psicosis en personas con antecedentes personales o familiares de trastornos psicóticos. Un peligro distinto y poco apreciado es comer el hongo equivocado, ya que varias especies mortales se parecen a las que contienen psilocibina.<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref6">[6]</a></sup></p>
        <p>En el análisis multicriterio de <em>Lancet</em> de 2010 dirigido por David Nutt, los hongos de psilocibina obtuvieron la puntuación más baja de daño combinado a usuarios y a terceros de 20 drogas, por debajo del cannabis, el alcohol, el tabaco y todas las demás sustancias evaluadas.<sup class="ref"><a href="#ref1">[1]</a></sup> Una revisión de 2011 encargada para la política de drogas neerlandesa llegó a una conclusión similar y describió el potencial de daño físico y psicológico de los hongos mágicos como bajo.<sup class="ref"><a href="#ref2">[2]</a></sup> Este artículo expone lo que muestra realmente la evidencia, dónde están los riesgos reales y cómo reducirlos.</p>
        <div class="toc">
            <div class="toc-title">Contenido</div>
            <ol>
                <li><a href="#short-answer">La respuesta breve</a></li>
                <li><a href="#side-effects">Efectos secundarios</a></li>
                <li><a href="#bad-trips">Malos viajes y riesgo psicológico</a></li>
                <li><a href="#mental-health">Salud mental, psicosis y HPPD</a></li>
                <li><a href="#overdose">¿Se puede sufrir una sobredosis? Toxicidad y envenenamiento</a></li>
                <li><a href="#emergency">Síntomas de emergencia</a></li>
                <li><a href="#interactions">Interacciones farmacológicas</a></li>
                <li><a href="#brain">Efectos en el cerebro</a></li>
                <li><a href="#who-should-avoid">Quién debería evitar la psilocibina</a></li>
                <li><a href="#harm-reduction">Reducción de daños</a></li>
                <li><a href="#risks-benefits">Riesgos frente a beneficios</a></li>
                <li><a href="#references">Referencias</a></li>
            </ol>
        </div>
        <h2 id="short-answer">La respuesta breve</h2>
        <p>¿Qué tan peligrosos son los hongos? En lo físico, muy poco. La psilocibina no tiene toxicidad orgánica conocida a las dosis que se toman, no deprime la respiración, y la dosis estimada necesaria para matar a una persona es del orden de mil veces una dosis eficaz típica.<sup class="ref"><a href="#ref3">[3]</a></sup> No se ha documentado ningún caso fiable de sobredosis mortal por hongos de psilocibina solos en un adulto sano; el puñado de muertes en la literatura implicó especies tóxicas de aspecto similar, enfermedad cardíaca preexistente, otras drogas o accidentes como caídas y ahogamientos bajo intoxicación.<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup></p>
        <p>En lo psicológico, el panorama es más matizado. En la encuesta más amplia de experiencias difíciles con psilocibina, el 39% de casi 2.000 personas encuestadas calificó su peor «mal viaje» entre las cinco experiencias más difíciles de su vida, el 11% dijo que se puso a sí misma o a otras en riesgo de daño físico durante el episodio, y el 7.6% buscó tratamiento por síntomas psicológicos persistentes después.<sup class="ref"><a href="#ref7">[7]</a></sup> La mayoría de esos episodios ocurrió sin un acompañante sobrio, en entornos no planificados o a dosis altas.</p>
        <div class="ambox">
            <strong>En síntesis:</strong> el peligro de los hongos mágicos proviene sobre todo de <em>lo que las personas hacen bajo los efectos</em>, de <em>quién los toma</em> (personas vulnerables a la psicosis), de <em>qué más hay en su organismo</em> (litio, ciertas otras drogas) y de <em>si el hongo es realmente psilocibina</em>. Cada uno de esos riesgos puede reducirse de forma sustancial.
        </div>
        <h2 id="side-effects">Efectos secundarios</h2>
        <p>Los efectos secundarios de los hongos mágicos se agrupan en tres categorías: físicos, perceptivos y psicológicos. Los efectos agudos comienzan 20&ndash;40 minutos después de la ingestión, alcanzan el máximo alrededor de 60&ndash;90 minutos y se resuelven en aproximadamente seis horas.<sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <table class="wikitable">
            <tr><th>Tipo</th><th>Efectos habituales</th><th>Notas</th></tr>
            <tr><td>Físicos</td><td>Náuseas, vómitos (habitualmente al inicio), dilatación pupilar, aumentos modestos de la frecuencia cardíaca y la presión arterial, sudoración, escalofríos, debilidad muscular, mala coordinación, bostezos</td><td>En ensayos controlados, la presión arterial y la frecuencia cardíaca suben de forma moderada y vuelven a la línea base en horas; las náuseas son la queja más frecuente.<sup class="ref"><a href="#ref8">[8]</a></sup><sup class="ref"><a href="#ref9">[9]</a></sup></td></tr>
            <tr><td>Perceptivos</td><td>Distorsión visual y patrones, sentido alterado del tiempo, sinestesia, intensificación del sonido y el color</td><td>Dependientes de la dosis; efectos esperados, no eventos adversos en sí.</td></tr>
            <tr><td>Psicológicos</td><td>Euforia, asombro, risa, apertura emocional; también ansiedad, miedo, paranoia, confusión, sensación de pérdida de control</td><td>En un estudio de dosis alta de Johns Hopkins, alrededor de un tercio de las personas voluntarias experimentó miedo o ansiedad significativos en algún momento de la sesión, incluso con una preparación cuidadosa.<sup class="ref"><a href="#ref10">[10]</a></sup></td></tr>
            <tr><td>Día siguiente</td><td>Fatiga, dolor de cabeza, ánimo bajo o, a la inversa, ánimo elevado («afterglow»)</td><td>El dolor de cabeza después de la psilocibina está relacionado con la dosis, comienza después de los efectos agudos y se resuelve en uno o dos días.<sup class="ref"><a href="#ref11">[11]</a></sup></td></tr>
        </table>
        <p>Un análisis agrupado de 110 personas voluntarias sanas en ocho estudios de laboratorio suizos encontró que la psilocibina en dosis de hasta 0.315 mg/kg no produjo daño perceptivo, psicológico ni físico persistente en ninguna persona participante durante el seguimiento.<sup class="ref"><a href="#ref9">[9]</a></sup></p>
        <h2 id="bad-trips">Malos viajes y riesgo psicológico</h2>
        <p>Un «mal viaje» es un episodio agudo de ansiedad intensa, pánico, paranoia, disforia o desorientación durante los efectos de la sustancia. Es la experiencia adversa grave más habitual asociada a los hongos mágicos y el motivo usual por el que las personas acuden a los servicios de urgencias.<sup class="ref"><a href="#ref12">[12]</a></sup> Los malos viajes están fuertemente ligados a la dosis, al estado mental («set») y al entorno («setting»).<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <p>La encuesta de 2016 de Carbonaro y colegas de 1,993 personas que habían tenido un viaje difícil con psilocibina encontró:<sup class="ref"><a href="#ref7">[7]</a></sup></p>
        <ul>
            <li>La dosis mediana en la peor experiencia fue de unos 4 gramos de hongos secos, aproximadamente una dosis alta.</li>
            <li>El 11% se puso a sí mismo o a otras personas en riesgo de daño físico; el 2.6% actuó de forma agresiva o violenta; el 2.7% buscó ayuda médica durante el episodio.</li>
            <li>Tres personas encuestadas con ansiedad, depresión o ideación suicida preexistentes intentaron suicidarse durante la experiencia.</li>
            <li>El 7.6% buscó tratamiento por síntomas psicológicos persistentes después.</li>
            <li>A pesar de ello, el 84% dijo que se benefició de la experiencia, y la dificultad se asoció de forma positiva con el significado personal comunicado.</li>
        </ul>
        <p>Estar solo, estar en un lugar desconocido o público y tomar una dosis mayor de la prevista hicieron más probable el daño. Esas son las variables que apunta la práctica de reducción de daños.</p>
        <h2 id="mental-health">Salud mental, psicosis y HPPD</h2>
        <p>El riesgo psiquiátrico más grave es precipitar un episodio psicótico prolongado en alguien predispuesto a trastornos psicóticos como la esquizofrenia o el trastorno bipolar I. Los ensayos clínicos excluyen a esas personas participantes, de modo que faltan datos prospectivos sobre este grupo; la exclusión misma refleja un consenso de que el riesgo es real.<sup class="ref"><a href="#ref13">[13]</a></sup><sup class="ref"><a href="#ref14">[14]</a></sup> Informes de casos describen psicosis, manía y desestabilización anímica prolongada tras el uso de hongos, habitualmente en personas con antecedentes personales o familiares de estas afecciones.<sup class="ref"><a href="#ref14">[14]</a></sup></p>
        <p>Para la población general, los grandes estudios epidemiológicos no han encontrado que el uso de psicodélicos eleve la tasa de problemas de salud mental. Un análisis de 130,152 adultos de EE. UU. en la National Survey on Drug Use and Health no encontró asociación entre el uso de psicodélicos a lo largo de la vida (incluida la psilocibina) y el malestar psicológico grave, el tratamiento de salud mental o los síntomas de pánico, depresión, ansiedad o psicosis; algunas asociaciones iban en dirección protectora.<sup class="ref"><a href="#ref15">[15]</a></sup> Un análisis de seguimiento de 190,000 adultos encontró de forma similar tasas más bajas de malestar psicológico y de suicidalidad en el mes previo entre quienes usaban psicodélicos clásicos.<sup class="ref"><a href="#ref16">[16]</a></sup> Estos son hallazgos correlacionales y no pueden descartar el riesgo en subgrupos vulnerables.</p>
        <p><strong>Trastorno perceptivo persistente por alucinógenos (HPPD)</strong>, en el que alteraciones visuales como estelas, halos o nieve visual persisten semanas o años, es un diagnóstico reconocido del DSM-5. Parece ser raro, se asocia con más frecuencia al LSD que a la psilocibina y no ocurrió en ninguna persona participante de la literatura moderna de ensayos controlados, aunque las encuestas poblacionales sugieren que los fenómenos transitorios de «flashback» no son raros y suelen desvanecerse.<sup class="ref"><a href="#ref17">[17]</a></sup></p>
        <h2 id="overdose">¿Se puede sufrir una sobredosis? Toxicidad y envenenamiento</h2>
        <p>Una «sobredosis» de hongos mágicos en el sentido de una dosis tóxica que pone en peligro la vida no es una preocupación práctica. El análisis comparativo de Robert Gable estimó la dosis letal de psilocibina en humanos en alrededor de 1,000 veces la dosis eficaz, frente a unas 10 para el alcohol y 6 para la heroína intravenosa.<sup class="ref"><a href="#ref3">[3]</a></sup> Los estudios en animales sitúan la dosis letal mediana de psilocibina en torno a 280 mg/kg en ratas, cientos de veces la dosis activa humana por kilogramo.<sup class="ref"><a href="#ref2">[2]</a></sup> Como un hongo seco contiene aproximadamente 0.5&ndash;1% de psilocibina en peso, alcanzar una cantidad físicamente letal comiendo hongos se considera en la práctica imposible.<sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref4">[4]</a></sup></p>
        <p>Lo que las personas suelen querer decir con «sobredosis» es tomar mucho más de lo previsto, lo que produce una experiencia abrumadora y aterradora más que daño orgánico. Los síntomas de una dosis muy alta incluyen confusión grave, incapacidad para comunicarse, agitación, pánico, vómitos y, en casos raros, convulsiones o temperatura alta, esto último comunicado con más frecuencia cuando había otras sustancias involucradas.<sup class="ref"><a href="#ref12">[12]</a></sup></p>
        <h3>Envenenamiento por hongos mal identificados</h3>
        <p>El escenario genuinamente letal que involucra «hongos mágicos» es comer una especie tóxica por error. Las especies mortales de <em>Amanita</em> y <em>Galerina</em>, que contienen amatoxinas que destruyen el hígado, pueden crecer en los mismos hábitats y parecerse de forma superficial a algunas especies de <em>Psilocybe</em>. El envenenamiento por amatoxinas es engañoso: los síntomas gastrointestinales aparecen 6&ndash;24 horas después de la ingestión, parecen mejorar y luego se desarrolla insuficiencia hepática en los días siguientes.<sup class="ref"><a href="#ref6">[6]</a></sup> Cualquier hongo comido del medio silvestre que produzca vómitos y diarrea retardados muchas horas después es una emergencia médica, no un mal viaje.</p>
        <p>Las exposiciones a psilocibina comunicadas a los centros de toxicología de EE. UU. aumentaron de forma pronunciada a principios de la década de 2020, con un incremento de más del triple entre adolescentes entre 2018 y 2022, y alrededor de tres cuartas partes de los casos adolescentes requirieron atención médica.<sup class="ref"><a href="#ref18">[18]</a></sup> La mayoría de los efectos comunicados fueron alucinaciones, agitación y taquicardia; los desenlaces graves fueron poco frecuentes.</p>
        <h3>Casos graves raros</h3>
        <p>Un número pequeño de informes de casos describe daño físico grave después del uso de hongos, incluida rabdomiólisis con lesión renal aguda, y un paro cardíaco mortal en una persona receptora de un trasplante de corazón cuyo corazón trasplantado no pudo responder con normalidad a los efectos autonómicos de la sustancia.<sup class="ref"><a href="#ref5">[5]</a></sup> Las complicaciones renales y cardíacas se asocian con más fuerza a otros géneros de hongos (por ejemplo <em>Cortinarius</em>) y a drogas coingeridas que a la psilocibina misma.<sup class="ref"><a href="#ref4">[4]</a></sup> Se documentan aquí porque existen, no porque sean típicas.</p>
        <h2 id="emergency">Síntomas de emergencia</h2>
        <div class="ambox warn">
            <strong>Llame al 911 o a Poison Control (1-800-222-1222) si la persona:</strong> no responde o no se la puede despertar; tiene una convulsión; tiene dolor torácico, un latido muy rápido o irregular, o dificultad para respirar; tiene una temperatura corporal alta con músculos rígidos o sudoración profusa (posible toxicidad serotoninérgica, sobre todo si hay otras drogas involucradas); es violenta, se autolesiona o intenta irse a un lugar peligroso; o desarrolla vómitos y diarrea <em>horas después</em> de comer hongos recolectados (posible envenenamiento por amatoxinas).
        </div>
        <p>Una persona que está asustada, confundida, llora o está convencida de que algo va mal, pero que está físicamente estable, no suele necesitar una ambulancia. Lo que ayuda es un acompañante sereno, un espacio quieto y seguro, la tranquilidad de que los efectos son temporales y pasarán en unas horas, y evitar la sujeción o la discusión.<sup class="ref"><a href="#ref19">[19]</a></sup> En caso de duda, llame a Poison Control; el servicio es gratuito, confidencial y puede aconsejar si se necesita atención hospitalaria.</p>
        <h2 id="interactions">Interacciones farmacológicas</h2>
        <ul>
            <li><strong>Litio</strong>: la interacción documentada más importante. En un análisis de 62 informes en línea de psicodélicos clásicos combinados con litio, el 47% implicó convulsiones y el 18% requirió atención médica de urgencia; la lamotrigina no mostró ese patrón.<sup class="ref"><a href="#ref20">[20]</a></sup> La psilocibina no debe combinarse con litio.</li>
            <li><strong>ISRS y IRSN</strong>: los antidepresivos suelen atenuar los efectos subjetivos de la psilocibina más que producir efectos peligrosos; el síndrome serotoninérgico por psilocibina sola no está documentado, pero es una preocupación teórica cuando se combina con IMAO o tramadol.<sup class="ref"><a href="#ref21">[21]</a></sup></li>
            <li><strong>IMAO</strong>: los inhibidores de la monoaminooxidasa pueden intensificar y prolongar los efectos de la psilocina de forma imprevisible.<sup class="ref"><a href="#ref21">[21]</a></sup></li>
            <li><strong>Alcohol y cannabis</strong>: ambos aumentan la probabilidad de náuseas, confusión y una experiencia difícil; el alcohol añade riesgo de lesiones.<sup class="ref"><a href="#ref12">[12]</a></sup></li>
            <li><strong>Estimulantes</strong>: la combinación con anfetaminas, MDMA o cocaína eleva aún más la frecuencia cardíaca y la presión arterial y aumenta el riesgo de ansiedad e hipertermia.</li>
        </ul>
        <h2 id="brain">Efectos en el cerebro</h2>
        <p>Los efectos de la psilocibina en el cerebro son el tema del artículo principal del sitio; aquí la pregunta es si esos efectos son dañinos. La psilocina actúa sobre todo en los receptores de serotonina 5-HT<sub>2A</sub>, reduce de forma transitoria la integridad de la red neuronal por defecto y aumenta la comunicación entre redes cerebrales que habitualmente están segregadas.<sup class="ref"><a href="#ref22">[22]</a></sup> Un estudio de 2024 en <em>Nature</em> encontró que una sola dosis alta desincronizó las redes corticales durante la duración de los efectos de la sustancia, con un cambio menor en la conexión hipocampo-red por defecto que persistió semanas.<sup class="ref"><a href="#ref23">[23]</a></sup></p>
        <p>Estos cambios se consideran la base tanto de la experiencia aguda como de los efectos terapéuticos comunicados, y ningún estudio ha encontrado evidencia de que la psilocibina dañe las neuronas. Los estudios en animales y en células sugieren lo contrario: mayor densidad de espinas dendríticas y expresión de genes relacionados con la neuroplasticidad.<sup class="ref"><a href="#ref24">[24]</a></sup> Si estos efectos de plasticidad podrían ser dañinos en un cerebro en desarrollo es desconocido; casi no hay datos controlados en adolescentes, lo que es una de las razones por las que se desaconseja el uso en jóvenes.<sup class="ref"><a href="#ref18">[18]</a></sup></p>
        <h2 id="who-should-avoid">Quién debería evitar la psilocibina</h2>
        <p>A partir de los criterios de exclusión usados en los ensayos clínicos y de las directrices de seguridad publicadas:<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <ul>
            <li>Personas con antecedentes personales o de familiar de primer grado de esquizofrenia, trastorno esquizoafectivo, trastorno bipolar I u otras afecciones psicóticas.</li>
            <li>Personas que toman litio, o quienes están con IMAO.</li>
            <li>Personas con hipertensión no controlada, ictus o infarto reciente, arritmia grave u otra enfermedad cardiovascular significativa, por el aumento transitorio de la presión arterial y la frecuencia cardíaca.</li>
            <li>Personas embarazadas o que amamantan (no hay datos de seguridad).</li>
            <li>Adolescentes y niños.</li>
            <li>Cualquier persona que esté en crisis aguda, gravemente intoxicada o sin un lugar seguro y una persona con quien estar.</li>
        </ul>
        <h2 id="harm-reduction">Reducción de daños</h2>
        <p>Las siguientes medidas abordan las fuentes documentadas de daño. Se extraen de las directrices de seguridad clínica<sup class="ref"><a href="#ref13">[13]</a></sup>, de la literatura de encuestas sobre experiencias difíciles<sup class="ref"><a href="#ref7">[7]</a></sup> y de organizaciones de reducción de daños como el Zendo Project y DanceSafe.<sup class="ref"><a href="#ref19">[19]</a></sup></p>
        <ol>
            <li><strong>Sepa lo que tiene.</strong> Nunca coma hongos recolectados a menos que una persona identificadora competente haya confirmado la especie. La identificación errónea es el único escenario con más probabilidad de ser mortal.</li>
            <li><strong>Hágase un cribado.</strong> Revise las contraindicaciones anteriores con honestidad, incluidos los antecedentes familiares y los medicamentos actuales.</li>
            <li><strong>Empiece por lo bajo.</strong> La potencia varía varias veces entre especies e incluso entre lotes. Una primera dosis de 1 gramo o menos de <em>Psilocybe cubensis</em> seco da una idea del efecto; la mediana de la encuesta para las peores experiencias fue de unos 4 gramos.</li>
            <li><strong>Tenga un acompañante sobrio.</strong> Una persona de confianza y sobria que pueda tranquilizar, redirigir y pedir ayuda si hace falta es la salvaguarda más eficaz contra el daño durante un mal viaje.</li>
            <li><strong>Elija el entorno.</strong> Privado, familiar, a salvo del tráfico, el agua, las alturas y la maquinaria pesada. No conduzca. Planifique quedarse en el mismo sitio durante seis horas.</li>
            <li><strong>No mezcle.</strong> Sobre todo no con litio, alcohol o estimulantes.</li>
            <li><strong>Prepárese para la dificultad.</strong> La ansiedad y el miedo son habituales y pasan. Respirar despacio, cambiar de habitación, cambiar la música y que le recuerden que la sustancia se desvanecerá son los apoyos habituales. «Confía, suelta, ábrete» es la frase usada en las sesiones de Johns Hopkins.<sup class="ref"><a href="#ref10">[10]</a></sup></li>
            <li><strong>Sepa cuándo llamar.</strong> Véase los síntomas de emergencia anteriores. Poison Control no involucra a las fuerzas del orden.</li>
            <li><strong>Integre después.</strong> Hablar de la experiencia con una persona de confianza o un terapeuta reduce la probabilidad de malestar persistente.</li>
        </ol>
        <h2 id="risks-benefits">Riesgos frente a beneficios</h2>
        <p>Los riesgos y beneficios de la psilocibina se sopesan cada vez más de forma formal. En el lado del beneficio, los ensayos aleatorizados han comunicado grandes reducciones de la depresión,<sup class="ref"><a href="#ref25">[25]</a></sup> y reducciones del consumo intenso de alcohol en el trastorno por uso de alcohol,<sup class="ref"><a href="#ref26">[26]</a></sup> habitualmente después de una o dos dosis supervisadas. En el lado del riesgo, los mismos ensayos comunican ansiedad transitoria, dolor de cabeza, náuseas y elevación de la presión arterial, y muy de vez en cuando malestar prolongado. En entornos supervisados con cribado médico, ningún ensayo ha comunicado una muerte, una psicosis persistente o un caso de HPPD.<sup class="ref"><a href="#ref9">[9]</a></sup><sup class="ref"><a href="#ref25">[25]</a></sup></p>
        <p>Esos resultados no se trasladan de forma directa al uso no supervisado, donde faltan el cribado, la precisión de la dosis y el apoyo que producen el historial de seguridad. La brecha entre la seguridad clínica y el riesgo en el mundo real es precisamente lo que la reducción de daños intenta cerrar.</p>
        <h2 id="see-also">Véase también</h2>
        <div class="see-also">
        <ul>
            <li><a href="/es/">Psilocibina</a>: panorama, farmacología, investigación y situación legal</li>
            <li><a href="/es/are-shrooms-addictive/">¿Crean adicción los hongos?</a>: dependencia, tolerancia y potencial de abuso</li>
            <li><a href="/es/events/">Acontecimientos recientes</a>: noticias de investigación y política</li>
        </ul>
        </div>
<div class="ambox help">
            <strong>Si alguien necesita ayuda ahora mismo:</strong> US Poison Control <strong>1-800-222-1222</strong> (24/7, gratuito, confidencial) &middot; Emergencias <strong>911</strong> &middot; Línea de apoyo entre pares psicodélico de Fireside Project <strong>62-FIRESIDE (623-473-7433)</strong> &middot; 988 Suicide &amp; Crisis Lifeline: llame o envíe un mensaje de texto al <strong>988</strong>.
        </div>
        <h2 id="references">Referencias</h2>
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

ADDICTION_CONTENT = r"""        <h1 class="page-title">¿Crean adicción los hongos?</h1>
        <p class="page-subtitle">De WikiPsilocybin, la enciclopedia libre de la psilocibina, un artículo de reducción de daños</p>
        <p class="hatnote">Este artículo cubre la dependencia y el potencial de abuso de los hongos de psilocibina. Sobre efectos secundarios, sobredosis y seguridad general, véase <a href="/es/are-magic-mushrooms-dangerous/">¿Son peligrosos los hongos mágicos?</a></p>
        <div class="infobox">
            <div class="infobox-title">Potencial de abuso de la psilocibina</div>
            <div class="infobox-row"><div class="infobox-label">Dependencia física</div><div class="infobox-value">No observada<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Síndrome de abstinencia</div><div class="infobox-value">Ninguno documentado<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Autoadministración en animales</div><div class="infobox-value">Débil o ausente; los animales no trabajan de forma fiable por la psilocibina<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref3">[3]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Tolerancia</div><div class="infobox-value">Se desarrolla en días; se restablece en gran medida después de 1&ndash;2 semanas<sup class="ref"><a href="#ref4">[4]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Recomendación experta de clasificación</div><div class="infobox-value">Lista IV (bajo potencial de abuso) si se aprueba médicamente<sup class="ref"><a href="#ref1">[1]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Clasificación actual en EE. UU.</div><div class="infobox-value">Lista I</div></div>
        </div>
        <p><strong>Los hongos de psilocibina («hongos» o «shrooms») no se consideran adictivos del modo en que lo son el alcohol, la nicotina, los opioides o los estimulantes.</strong> No producen dependencia física ni un síndrome de abstinencia, los animales de laboratorio no se los autoadministran de forma fiable, y la tolerancia rápida que producen hace que el uso diario se limite por sí mismo.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref4">[4]</a></sup> Una revisión exhaustiva de la psilocibina frente a los ocho factores de potencial de abuso de la Controlled Substances Act de EE. UU. concluyó que, si se aprobara como medicamento, encajaría en la Lista IV, la categoría de drogas con bajo potencial de abuso como las benzodiazepinas y el zolpidem, y no en la Lista I donde se sitúa ahora.<sup class="ref"><a href="#ref1">[1]</a></sup></p>
        <p>Eso no significa que el uso problemático sea imposible. Una minoría de personas usa alucinógenos de forma lo bastante compulsiva como para cumplir criterios de <em>trastorno por uso de alucinógenos</em>, un diagnóstico del DSM-5, y pueden formarse hábitos psicológicos en torno a cualquier experiencia que una persona encuentre significativa o evasiva.<sup class="ref"><a href="#ref5">[5]</a></sup> Este artículo explica la distinción, lo que dice la evidencia y el pequeño número de situaciones en las que el uso de hongos merece atención.</p>
        <div class="toc">
            <div class="toc-title">Contenido</div>
            <ol>
                <li><a href="#short-answer">La respuesta breve</a></li>
                <li><a href="#what-addiction-means">Qué significa «adictivo»</a></li>
                <li><a href="#evidence">La evidencia</a></li>
                <li><a href="#tolerance">La tolerancia y por qué importa</a></li>
                <li><a href="#withdrawal">Abstinencia</a></li>
                <li><a href="#use-disorder">Trastorno por uso de alucinógenos</a></li>
                <li><a href="#microdosing">¿Cambia el panorama la microdosis?</a></li>
                <li><a href="#treatment">La psilocibina como tratamiento de la adicción</a></li>
                <li><a href="#harm-reduction">Reducción de daños</a></li>
                <li><a href="#references">Referencias</a></li>
            </ol>
        </div>
        <h2 id="short-answer">La respuesta breve</h2>
        <p>No, según las definiciones científicas habituales. El National Institute on Drug Abuse de EE. UU. afirma que no se sabe que la psilocibina cause dependencia física, y la propia ficha de la Drug Enforcement Administration señala que la psilocibina no produce conducta compulsiva de búsqueda de la droga en modelos animales.<sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref6">[6]</a></sup> En el análisis multicriterio de daño de <em>Lancet</em> de 2010, los hongos de psilocibina obtuvieron la puntuación más baja de 20 drogas en el criterio de «dependencia» y también en el daño global.<sup class="ref"><a href="#ref7">[7]</a></sup></p>
        <p>Los rasgos que hacen adictiva una droga, es decir, una activación fuerte de la vía de recompensa dopaminérgica del cerebro, un uso creciente, abstinencia física y ansia entre usos, son débiles o están ausentes en la psilocibina. La mayoría de las personas que prueban hongos los usan un puñado de veces en su vida; la National Survey on Drug Use and Health encuentra de forma consistente que el uso en el mes previo es una fracción pequeña del uso a lo largo de la vida, un patrón opuesto al de las drogas adictivas.<sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <h2 id="what-addiction-means">Qué significa «adictivo»</h2>
        <p>Quienes investigan la adicción distinguen varias cosas a las que puede referirse «adictivo»:</p>
        <ul>
            <li><strong>Dependencia física</strong>: el cuerpo se adapta a la droga de modo que dejarla causa un síndrome de abstinencia (alcohol, opioides, benzodiazepinas).</li>
            <li><strong>Refuerzo</strong>: la droga activa de forma directa los circuitos de recompensa de modo que animales y personas trabajarán para obtenerla de forma repetida (cocaína, nicotina).</li>
            <li><strong>Uso compulsivo</strong>: uso continuado a pesar del daño, pérdida de control, ansia; este es el núcleo de un trastorno por uso de sustancias del DSM-5.</li>
            <li><strong>Hábito psicológico</strong>: dependencia de una experiencia para afrontar o evadirse, que puede adherirse a casi cualquier actividad.</li>
        </ul>
        <p>La psilocibina puntúa bajo en los tres primeros y, como cualquier experiencia potente, no es inmune al cuarto.</p>
        <h2 id="evidence">La evidencia</h2>
        <h3>Estudios en animales</h3>
        <p>La prueba de laboratorio habitual de potencial de abuso es si los animales se autoadministrarán una droga. Las ratas y los monos se autoadministran con facilidad cocaína, heroína, nicotina y alcohol. Los psicodélicos clásicos, incluida la psilocibina, están entre las pocas drogas psicoactivas que los animales no se autoadministran de forma fiable, y en las pruebas de preferencia de lugar condicionada producen preferencia débil o nula.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref3">[3]</a></sup> La psilocina tampoco aumenta de forma sustancial la dopamina en el núcleo accumbens, la firma de las drogas reforzantes, aunque tiene efectos dopaminérgicos indirectos modestos.<sup class="ref"><a href="#ref3">[3]</a></sup></p>
        <h3>Estudios clínicos y de laboratorio en humanos</h3>
        <p>En más de dos décadas de ensayos clínicos modernos con más de mil personas participantes que recibieron psilocibina bajo supervisión, ningún estudio ha comunicado búsqueda de la droga, ansia o uso compulsivo posterior como desenlace.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref9">[9]</a></sup> Un metaanálisis de 2024 de eventos adversos en ensayos de psicodélicos clásicos no encontró casos de dependencia.<sup class="ref"><a href="#ref9">[9]</a></sup> El seguimiento de personas voluntarias sanas en los estudios de Johns Hopkins encontró que el cambio más habitual en el uso de drogas después de una sesión de dosis alta fue un <em>descenso</em> del uso de otras sustancias.<sup class="ref"><a href="#ref10">[10]</a></sup></p>
        <h3>Datos poblacionales</h3>
        <p>Entre los adultos de EE. UU., el uso de psilocibina a lo largo de la vida es habitual (alrededor de uno de cada diez), pero el uso regular es raro. Los análisis de la National Survey on Drug Use and Health no encontraron asociación entre el uso de psicodélicos a lo largo de la vida y un aumento de los problemas de salud mental, y algunos análisis encontraron que el uso de psicodélicos se asociaba con menores probabilidades de trastorno por uso de opioides.<sup class="ref"><a href="#ref8">[8]</a></sup><sup class="ref"><a href="#ref11">[11]</a></sup></p>
        <h2 id="tolerance">La tolerancia y por qué importa</h2>
        <p>La psilocibina produce una tolerancia rápida y pronunciada. Tomar una segunda dosis en uno o dos días produce un efecto marcadamente más débil, y la dosificación diaria durante unos pocos días puede abolir el efecto psicodélico casi por completo; la sensibilidad vuelve después de aproximadamente una o dos semanas de abstinencia.<sup class="ref"><a href="#ref4">[4]</a></sup> Esto se debe a la regulación a la baja de los receptores 5-HT<sub>2A</sub> sobre los que actúa la psilocina, y se aplica de forma cruzada al LSD y a la mescalina.<sup class="ref"><a href="#ref4">[4]</a></sup></p>
        <p>La tolerancia rápida es una de las principales razones farmacológicas por las que la psilocibina es difícil de usar de forma compulsiva: el uso diario creciente simplemente deja de funcionar. Contrasta de forma nítida con drogas como los opioides, donde la tolerancia impulsa dosis más altas en lugar de quitar el incentivo a volver a dosificar.</p>
        <h2 id="withdrawal">Abstinencia</h2>
        <p>No se ha documentado un síndrome de abstinencia física para la psilocibina en humanos ni en animales, y no figura entre las sustancias con un síndrome de abstinencia reconocido en el DSM-5.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup> Quienes dejan de usarla después de un periodo de uso frecuente pueden notar un «bajón» de fatiga, ánimo bajo o aplanamiento durante uno o dos días después de sesiones individuales, pero esto es un efecto posterior de la experiencia más que un síndrome de dependencia, y no impulsa a volver a dosificar.<sup class="ref"><a href="#ref12">[12]</a></sup></p>
        <h2 id="use-disorder">Trastorno por uso de alucinógenos</h2>
        <p>El DSM-5 incluye el «trastorno por uso de otros alucinógenos» (distinto de la fenciclidina), que puede diagnosticarse cuando una persona muestra un patrón problemático de uso, por ejemplo dedicar tiempo excesivo a obtener o usar, abandonar actividades importantes o continuar a pesar del daño.<sup class="ref"><a href="#ref5">[5]</a></sup> Como la tolerancia cuenta como un criterio y la abstinencia no aplica, el diagnóstico se apoya sobre todo en criterios conductuales. La prevalencia es baja: el DSM-5 cita una prevalencia a 12 meses de alrededor del 0.1% entre los adultos de EE. UU., y en las poblaciones que buscan tratamiento los alucinógenos rara vez son la droga principal.<sup class="ref"><a href="#ref5">[5]</a></sup><sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <p>Las señales de alerta de que el uso se ha vuelto problemático se parecen a las de cualquier sustancia: usar con más frecuencia de la prevista, usar para evitar afrontar la vida más que para comprometerse con ella, un uso que interfiere con el trabajo, las relaciones o la seguridad, y dificultad para parar a pesar de querer hacerlo. Como la psilocibina no produce dependencia física, la respuesta adecuada es el apoyo psicológico más que la desintoxicación médica. La National Helpline de SAMHSA (1-800-662-4357) ofrece derivaciones gratuitas y confidenciales.<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <h2 id="microdosing">¿Cambia el panorama la microdosis?</h2>
        <p>La microdosis, tomar cantidades subperceptuales cada pocos días, es el único patrón de uso de psilocibina que es habitual por diseño. Incluso aquí, no se ha observado dependencia en el sentido farmacológico, y la mayoría de los protocolos incluyen días de descanso precisamente por la tolerancia.<sup class="ref"><a href="#ref14">[14]</a></sup> Las preguntas abiertas con la microdosis conciernen a la eficacia (los estudios controlados con placebo muestran que la mayoría de los beneficios comunicados los iguala el placebo) y a la falta de datos de seguridad a largo plazo sobre la activación repetida de los receptores 5-HT<sub>2B</sub>, una preocupación teórica de válvula cardíaca, más que a la adicción.<sup class="ref"><a href="#ref14">[14]</a></sup><sup class="ref"><a href="#ref15">[15]</a></sup></p>
        <h2 id="treatment">La psilocibina como tratamiento de la adicción</h2>
        <p>En lugar de causar adicción, la psilocibina se estudia como tratamiento de ella. En un ensayo aleatorizado de 2022 en NYU, dos sesiones supervisadas de psilocibina combinadas con terapia redujeron los días de consumo intenso de alcohol en personas con trastorno por uso de alcohol en un 83% a lo largo de ocho meses, frente a un 51% con un placebo activo.<sup class="ref"><a href="#ref16">[16]</a></sup> Un estudio piloto de Johns Hopkins de psilocibina para el cese del tabaco comunicó un 80% de abstinencia verificada biológicamente a los seis meses y un 60% a los 30 meses, muy por encima de las tasas de los tratamientos convencionales, aunque el estudio fue pequeño y no controlado.<sup class="ref"><a href="#ref17">[17]</a></sup> Hay en marcha ensayos más grandes en trastornos por uso de alcohol, tabaco, opioides y cocaína.</p>
        <h2 id="harm-reduction">Reducción de daños</h2>
        <p>Como el riesgo de adicción es bajo, la reducción de daños para los hongos se centra en los riesgos agudos cubiertos en <a href="/es/are-magic-mushrooms-dangerous/">¿Son peligrosos los hongos mágicos?</a>: identificación de hongos, dosis, entorno, un acompañante sobrio y evitar combinaciones con litio, alcohol y estimulantes. Específico de los patrones de uso:</p>
        <ul>
            <li><strong>Separe las sesiones.</strong> La tolerancia significa que volver a dosificar en cuestión de días se desperdicia en gran medida y añade esfuerzo físico sin efecto. Muchas personas usuarias experimentadas y clínicas sugieren semanas o meses entre dosis completas.</li>
            <li><strong>Note el motivo.</strong> Usar para explorar, celebrar o procesar es distinto de usar para evitar. Si los hongos se han convertido en el modo de afrontar algo, ese algo sigue necesitando atención.</li>
            <li><strong>Vigile otras sustancias.</strong> Las personas que desarrollan problemas en torno a los psicodélicos tienen con frecuencia un uso problemático concurrente de alcohol o cannabis; esas suelen ser las drogas que hay que abordar primero.</li>
            <li><strong>Los antecedentes de salud mental importan más que el riesgo de adicción.</strong> La razón principal para ser cauto con el uso repetido es la vulnerabilidad psiquiátrica, no la dependencia.</li>
        </ul>
        <h2 id="see-also">Véase también</h2>
        <div class="see-also">
        <ul>
            <li><a href="/es/are-magic-mushrooms-dangerous/">¿Son peligrosos los hongos mágicos?</a>: efectos secundarios, malos viajes, sobredosis e interacciones farmacológicas</li>
            <li><a href="/es/">Psilocibina</a>: panorama, farmacología, investigación y situación legal</li>
            <li><a href="/es/#therapeutic">Aplicaciones terapéuticas</a>: ensayos en trastornos por uso de sustancias</li>
        </ul>
        </div>
<div class="ambox help">
            <strong>Si alguien necesita ayuda ahora mismo:</strong> US Poison Control <strong>1-800-222-1222</strong> (24/7, gratuito, confidencial) &middot; Emergencias <strong>911</strong> &middot; SAMHSA National Helpline <strong>1-800-662-4357</strong> &middot; Línea de apoyo entre pares psicodélico de Fireside Project <strong>62-FIRESIDE (623-473-7433)</strong> &middot; 988 Suicide &amp; Crisis Lifeline: llame o envíe un mensaje de texto al <strong>988</strong>.
        </div>
        <h2 id="references">Referencias</h2>
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
            "description": "WikiPsilocybin es una enciclopedia independiente de investigación sobre psilocibina, ensayos clínicos, noticias legales y reducción de daños. Cada afirmación está citada a una fuente primaria.",
            "content": HOME_CONTENT,
            "extra_nav": True,
        },
        {
            "page": "/are-magic-mushrooms-dangerous/",
            "title": "¿Son peligrosos los hongos mágicos? Riesgos, efectos secundarios y seguridad | WikiPsilocybin",
            "description": "¿Son peligrosos los hongos mágicos? Una revisión basada en evidencia de los riesgos de la psilocibina: efectos secundarios, malos viajes, sobredosis y síntomas de envenenamiento, interacciones farmacológicas, contraindicaciones de salud mental y reducción de daños. Completamente referenciada.",
            "content": DANGER_CONTENT,
            "extra_nav": False,
        },
        {
            "page": "/are-shrooms-addictive/",
            "title": "¿Crean adicción los hongos? Dependencia, tolerancia y abstinencia | WikiPsilocybin",
            "description": "¿Crean adicción los hongos? Lo que dice la investigación sobre la dependencia de la psilocibina, la tolerancia, la abstinencia y el trastorno por uso de alucinógenos, y por qué los expertos califican su potencial de abuso como bajo. Completamente referenciada.",
            "content": ADDICTION_CONTENT,
            "extra_nav": False,
        },
    ]
    for spec in pages:
        html = render_page(
            lang="es",
            page=spec["page"],
            title=spec["title"],
            description=spec["description"],
            content=spec["content"],
            active_tab="article",
            extra_nav=spec["extra_nav"],
        )
        dest = write_page("es", spec["page"], html)
        print(f"wrote {dest}")


if __name__ == "__main__":
    main()
