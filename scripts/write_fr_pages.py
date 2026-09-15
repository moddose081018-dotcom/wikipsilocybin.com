#!/usr/bin/env python3
"""Write French translations of the homepage and two safety guides."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from i18n_chrome import render_page, write_page

HOME_CONTENT = r"""        <h1 class="page-title">Psilocybine</h1>
        <p class="page-subtitle">Depuis WikiPsilocybin, l'encyclopédie libre de la psilocybine, mise à jour quotidiennement</p>

        <div class="infobox">
            <div class="infobox-title">Psilocybine</div>
            <div class="infobox-image">
                <img src="https://d8j0ntlcm91z4.cloudfront.net/user_36uL1HV6CQZ9Ia0ikUE78jQJB98/hf_20260808_070842_c807ec80-0269-48c6-a459-06b22fa82a97.png" alt="Visualisation moléculaire de la psilocybine">
                <div class="caption">Illustration de la connectivité d'un réseau neuronal (représentation artistique, ce n'est pas une image de recherche)</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Formule</div>
                <div class="infobox-value">C&#8321;&#8322;H&#8321;&#8327;N&#8322;O&#8324;P</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Masse molaire</div>
                <div class="infobox-value">284.25 g/mol</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Premier isolement</div>
                <div class="infobox-value">1958, par Albert Hofmann</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Espèces connues</div>
                <div class="infobox-value">plus de 200 champignons</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Essais cliniques</div>
                <div class="infobox-value">plus de 400 enregistrés</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Usage humain</div>
                <div class="infobox-value">~6 000 ans documentés</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Statut juridique</div>
                <div class="infobox-value">Variable ; Tableau I (fédéral américain), usage thérapeutique légal en OR, CO, AU</div>
            </div>
        </div>

        <div id="recent-events" class="recent-events">
            <h3>Événements récents</h3>
            <ul class="event-list">
                <li>
                    <span class="event-date">6 août 2026</span>
                    <span class="event-tag tag-policy">Politique</span>
                    <span class="event-link"><a href="/events/2026-08-06-va-pivot-trial/">VA launches PIVOT, a five-site randomized trial of psilocybin for veterans with treatment-resistant depression</a></span>
                </li>
                <li>
                    <span class="event-date">30 juil. 2026</span>
                    <span class="event-tag tag-research">Recherche</span>
                    <span class="event-link"><a href="/events/2026-07-30-osu-veterans-ptsd-pilot/">Ohio State pilot trial: 9 of 12 veterans with severe, treatment-resistant PTSD in remission one month after psilocybin-assisted therapy</a></span>
                </li>
                <li>
                    <span class="event-date">26 janv. 2026</span>
                    <span class="event-tag tag-culture">Culture</span>
                    <span class="event-link"><a href="/events/2026-01-26-rand-psychedelic-use-survey/">RAND survey: about 11 million US adults used psilocybin in 2025, and most past-year users microdosed</a></span>
                </li>
                <li>
                    <span class="event-date">31 mars 2025</span>
                    <span class="event-tag tag-policy">Politique</span>
                    <span class="event-link"><a href="/events/2025-03-31-colorado-first-healing-center/">Colorado issues its first licensed psilocybin healing center license to The Center Origin in Denver</a></span>
                </li>
                <li>
                    <span class="event-date">17 juil. 2024</span>
                    <span class="event-tag tag-research">Recherche</span>
                    <span class="event-link"><a href="/events/2024-07-17-washu-psilocybin-desynchronizes-brain/">Washington University study in Nature shows psilocybin desynchronizes the brain's default mode network, with some changes lasting weeks</a></span>
                </li>
            </ul>
            <span class="view-all-link"><a href="/fr/events/">Voir tous les événements &rarr;</a></span>
        </div>

        <div class="toc">
            <div class="toc-title">Sommaire</div>
            <ol>
                <li><a href="#what-is">Qu'est-ce que la psilocybine ?</a></li>
                <li><a href="#how-it-works">Comment ça agit</a></li>
                <li><a href="#research">Recherche et essais cliniques</a></li>
                <li><a href="#therapeutic">Applications thérapeutiques</a></li>
                <li><a href="#microdosing">Microdosage</a></li>
                <li><a href="#legal">Statut juridique</a></li>
                <li><a href="#safety">Sécurité et réduction des risques</a></li>
            </ol>
        </div>

        <h2 id="what-is">Qu'est-ce que la psilocybine ?</h2>
        <p>La psilocybine est un composé psychédélique d'origine naturelle produit par plus de 200 espèces de champignons, habituellement appelés « champignons magiques ». Après ingestion, le corps convertit la psilocybine en psilocine, qui interagit avec les récepteurs de la sérotonine dans le cerveau et produit des états de conscience altérés, des changements visuels et auditifs, et des transformations profondes de la perception et de la pensée.</p>
        <p>Isolée et synthétisée pour la première fois par le chimiste suisse Albert Hofmann en 1958, la psilocybine est utilisée dans des pratiques cérémonielles autochtones depuis des milliers d'années. Les données archéologiques suggèrent un usage humain de champignons à psilocybine remontant à au moins 6 000 ans dans les cultures mésoaméricaines.</p>

        <h2 id="how-it-works">Comment ça agit</h2>
        <p>La psilocybine est un promédicament : biologiquement inactive jusqu'à ce que le corps la métabolise. Après ingestion, les enzymes phosphatase alcaline de l'intestin et du foie retirent un groupe phosphate et convertissent la psilocybine en psilocine (4-hydroxy-N,N-diméthyltryptamine).</p>
        <p>Le principal mécanisme d'action de la psilocine est l'agonisme des récepteurs de la sérotonine 5-HT<sub>2A</sub> dans le cortex préfrontal. Cela déclenche une cascade d'effets :</p>
        <ul>
            <li><strong>Interruption du réseau du mode par défaut (DMN)</strong> : réduit l'activité du système « pilote automatique » du cerveau et permet la formation de nouvelles connexions neuronales</li>
            <li><strong>Connectivité neuronale accrue</strong> : des régions cérébrales qui ne communiquent habituellement pas commencent à interagir et produisent des expériences synesthésiques et associatives</li>
            <li><strong>Promotion de la neuroplasticité</strong> : stimule la croissance dendritique et la densité synaptique, en particulier dans le cortex préfrontal et l'hippocampe</li>
            <li><strong>Traitement émotionnel</strong> : augmente la réponse de l'amygdale aux stimuli émotionnels et réduit la réactivité fondée sur la peur</li>
        </ul>
        <div class="ambox">
            <strong>Durée des effets :</strong> Le début survient généralement 20&ndash;40 minutes après l'ingestion. Les effets maximaux durent 2&ndash;3 heures, pour une durée totale de 4&ndash;6 heures. Des effets résiduels sur l'humeur et la cognition peuvent persister des jours ou des semaines.
        </div>

        <h2 id="research">Recherche et essais cliniques</h2>
        <p>La dernière décennie a vu une résurgence sans précédent de la recherche sur la psilocybine, avec des institutions majeures comme Johns Hopkins, Imperial College London, NYU et Yale qui mènent des essais cliniques rigoureux.</p>

        <h3>Jalons clés de la recherche</h3>
        <ul>
            <li><strong>2016 :</strong> Johns Hopkins et NYU publient simultanément des études de référence montrant que la psilocybine produit des baisses substantielles et durables de l'anxiété et de la dépression chez des patients atteints de cancer</li>
            <li><strong>2020 :</strong> Le Johns Hopkins Center for Psychedelic &amp; Consciousness Research est créé avec 17 millions de dollars de financement</li>
            <li><strong>2021 :</strong> JAMA Psychiatry publie un essai randomisé montrant que la thérapie à la psilocybine est au moins aussi efficace que l'escitalopram (Lexapro) pour le trouble dépressif majeur</li>
            <li><strong>2023 :</strong> La FDA accorde la désignation Breakthrough Therapy à la thérapie assistée par psilocybine pour la dépression résistante au traitement</li>
            <li><strong>2024&ndash;2026 :</strong> Plusieurs essais cliniques de phase 3 en cours ou achevés pour la dépression, le TSPT, l'addiction et la détresse en fin de vie</li>
        </ul>
        <div class="ambox">
            <strong>Nombre actuel d'essais :</strong> En 2026, plus de 400 essais cliniques enregistrés impliquant la psilocybine figurent sur ClinicalTrials.gov, couvrant des indications allant de la dépression majeure à l'anorexie, les céphalées en grappe et le trouble de l'usage d'opioïdes.
        </div>

        <h2 id="therapeutic">Applications thérapeutiques</h2>
        <p>La thérapie assistée par psilocybine combine les effets pharmacologiques de la psilocybine avec un accompagnement psychothérapeutique structuré. Les données actuelles étayent son potentiel pour traiter :</p>
        <ul>
            <li><strong>Trouble dépressif majeur (MDD)</strong> : taux de réponse de 60&ndash;80 % dans les essais cliniques, avec des effets durant 3&ndash;12 mois après 1&ndash;2 séances</li>
            <li><strong>Dépression résistante au traitement (TRD)</strong> : désignation Breakthrough Therapy de la FDA accordée ; essais de phase 3 en cours</li>
            <li><strong>Détresse en fin de vie</strong> : réduit l'anxiété existentielle et la dépression chez les patients atteints d'un cancer en phase terminale</li>
            <li><strong>TSPT</strong> : des données émergentes d'études centrées sur les vétérans montrent une réduction significative des symptômes</li>
            <li><strong>Troubles de l'usage de substances</strong> : résultats prometteurs pour l'arrêt du tabac et de l'alcool, avec des taux d'abandon 2&ndash;3 fois supérieurs à ceux des traitements conventionnels</li>
            <li><strong>Céphalées en grappe</strong> : soulagement rapporté par les patients et soutien clinique croissant</li>
        </ul>

        <h2 id="microdosing">Microdosage</h2>
        <p>Le microdosage consiste à prendre des doses subperceptuelles de psilocybine : habituellement 50&ndash;200 mg de matériel de champignon séché, soit environ 1/10 à 1/20 d'une dose complète. Les personnes qui le pratiquent rapportent des améliorations de la créativité, de la concentration, de la régulation émotionnelle et du bien-être général sans éprouver d'effets psychédéliques.</p>
        <p>Bien que les témoignages anecdotiques soient nombreux, la recherche contrôlée sur le microdosage reste limitée. Parmi les études notables :</p>
        <ul>
            <li>L'étude d'auto-insu de 2022 de The Beckley Foundation, qui a trouvé que certains bénéfices persistaient même dans le groupe placebo, ce qui suggère que les effets d'attente jouent un rôle</li>
            <li>L'étude de 2023 de la University of British Columbia montrant que les personnes qui prenaient des microdoses rapportaient une meilleure humeur et moins d'anxiété que celles qui n'en prenaient pas</li>
            <li>Des essais en cours financés par le NIH évaluant des protocoles standardisés de microdosage pour le renforcement cognitif et les troubles de l'humeur</li>
        </ul>

        <h2 id="legal">Statut juridique</h2>
        <p>Le paysage juridique de la psilocybine évolue rapidement dans le monde :</p>
        <h3>États-Unis</h3>
        <ul>
            <li><strong>Oregon</strong> : premier État à légaliser la thérapie réglementée à la psilocybine (Measure 109, 2020), avec des centres de service titulaires d'une licence en activité depuis 2023</li>
            <li><strong>Colorado</strong> : la Proposition 122 (2022) a dépénalisé la psilocybine et créé un cadre d'accès réglementé pour usage thérapeutique</li>
            <li><strong>Dépénalisation municipale</strong> : des villes comme Denver, Oakland, Santa Cruz, Seattle, Detroit et d'autres ont abaissé la priorité de l'application de la loi</li>
            <li><strong>Fédéral</strong> : la psilocybine reste au Tableau I de la Controlled Substances Act, bien que la législation bipartisane pour des exemptions de recherche continue d'avancer</li>
        </ul>

        <h3>International</h3>
        <ul>
            <li><strong>Canada</strong> : le Special Access Program permet aux professionnels de santé de demander de la psilocybine pour des affections résistantes au traitement</li>
            <li><strong>Australie</strong> : la TGA a approuvé la psilocybine pour la dépression résistante au traitement dans des cadres de psychiatres autorisés (juillet 2023)</li>
            <li><strong>Jamaïque et Pays-Bas</strong> : truffes/champignons à psilocybine disponibles via des zones grises juridiques ou une légalité explicite</li>
            <li><strong>Union européenne</strong> : plusieurs pays explorent des cadres réglementaires ; les essais cliniques s'étendent en Allemagne, au Royaume-Uni et en Suisse</li>
        </ul>

        <h2 id="safety">Sécurité et réduction des risques</h2>
        <p class="hatnote">Articles principaux : <a href="/fr/are-magic-mushrooms-dangerous/">Les champignons magiques sont-ils dangereux ?</a> et <a href="/fr/are-shrooms-addictive/">Les champignons créent-ils une addiction ?</a></p>
        <p>La psilocybine a un profil de sécurité bien établi par rapport aux autres substances psychoactives. Sa dose létale estimée est environ 1 000 fois une dose efficace typique, aucune surdose mortelle par psilocybine seule n'a été documentée de façon fiable chez un adulte en bonne santé, elle ne produit ni dépendance physique ni sevrage, et la tolérance rapide décourage l'usage fréquent. L'analyse multicritère de 2010 dans <em>Lancet</em> de David Nutt et ses collègues a classé les champignons à psilocybine comme les moins nocifs de 20 drogues récréatives en tenant compte à la fois du préjudice pour les usagers et du préjudice pour autrui.</p>
        <p>Les risques qui existent sont surtout psychologiques et situationnels, plutôt que toxiques :</p>
        <ul>
            <li><strong>Mauvais trips</strong> : anxiété aiguë, panique ou confusion ; dans une enquête sur près de 2 000 expériences difficiles, 11 % des personnes interrogées se sont mises elles-mêmes ou d'autres en danger physique et 7.6 % ont ensuite cherché un traitement pour des symptômes persistants</li>
            <li><strong>Vulnérabilité psychiatrique</strong> : non recommandé aux personnes ayant des antécédents personnels ou familiaux de troubles psychotiques ou de bipolarité de type I</li>
            <li><strong>Interactions médicamenteuses</strong> : le lithium est associé à des convulsions lorsqu'il est combiné avec des psychédéliques ; les ISRS atténuent les effets ; les IMAO peuvent les intensifier</li>
            <li><strong>Cardiovasculaire</strong> : augmentations modérées et transitoires de la fréquence cardiaque et de la pression artérielle ; prudence en cas de maladie cardiaque préexistante</li>
            <li><strong>Identification erronée</strong> : des espèces mortelles d'<em>Amanita</em> et de <em>Galerina</em> peuvent ressembler aux champignons à psilocybine ; les champignons cueillis sont la principale source d'empoisonnements mortels par « champignons magiques »</li>
            <li><strong>Set et setting</strong> : un accompagnateur sobre, un environnement privé sûr et une dose prudente sont les sauvegardes les plus efficaces</li>
        </ul>
        <div class="ambox">
            <strong>Besoin d'aide maintenant ?</strong> US Poison Control 1-800-222-1222 (gratuit, confidentiel, 24/7) &middot; Fireside Project soutien par les pairs psychédélique 62-FIRESIDE (623-473-7433) &middot; 988 Suicide &amp; Crisis Lifeline. Pour le détail complet et les références, voir <a href="/fr/are-magic-mushrooms-dangerous/">Les champignons magiques sont-ils dangereux ?</a>
        </div>
"""

DANGER_CONTENT = r"""        <h1 class="page-title">Les champignons magiques sont-ils dangereux ?</h1>
        <p class="page-subtitle">Depuis WikiPsilocybin, l'encyclopédie libre de la psilocybine, un article de réduction des risques</p>
        <p class="hatnote">Cet article couvre les risques, les effets secondaires et la sécurité des champignons à psilocybine (« champignons » ou « shrooms »). Sur le composé lui-même, voir <a href="/fr/">Psilocybine</a>. Sur la dépendance et le potentiel d'abus, voir <a href="/fr/are-shrooms-addictive/">Les champignons créent-ils une addiction ?</a></p>
        <div class="infobox">
            <div class="infobox-title">Sécurité des champignons à psilocybine</div>
            <div class="infobox-row"><div class="infobox-label">Toxicité physique</div><div class="infobox-value">Très faible ; le rapport dose létale/dose efficace est estimé près de 1,000:1<sup class="ref"><a href="#ref3">[3]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Décès confirmés par psilocybine seule</div><div class="infobox-value">Pratiquement aucun dans la littérature ; les décès impliquent des champignons toxiques mal identifiés, des accidents ou des drogues co-ingérées<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Principaux risques</div><div class="infobox-value">Détresse psychologique (« mauvais trip »), conduite à risque sous l'effet, psychose chez les personnes vulnérables, interactions médicamenteuses, identification erronée de champignons</div></div>
            <div class="infobox-row"><div class="infobox-label">Classement global du préjudice</div><div class="infobox-value">Le plus bas de 20 drogues dans l'analyse multicritère de <em>Lancet</em> de 2010<sup class="ref"><a href="#ref1">[1]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Poison Control (États-Unis)</div><div class="infobox-value">1-800-222-1222</div></div>
        </div>
        <p><strong>Les champignons magiques figurent parmi les drogues récréatives physiquement les moins dangereuses qui ont été étudiées, mais ils ne sont pas sans risque.</strong> Les dangers principaux sont psychologiques plutôt que toxicologiques : des expériences terrifiantes ou déstabilisantes, des accidents sous l'effet, et le déclenchement d'une psychose chez des personnes ayant des antécédents personnels ou familiaux de troubles psychotiques. Un danger distinct et peu apprécié est de manger le mauvais champignon, car plusieurs espèces mortelles ressemblent à celles qui contiennent de la psilocybine.<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref6">[6]</a></sup></p>
        <p>Dans l'analyse multicritère de <em>Lancet</em> de 2010 dirigée par David Nutt, les champignons à psilocybine ont obtenu le score le plus bas de préjudice combiné pour les usagers et pour autrui parmi 20 drogues, en dessous du cannabis, de l'alcool, du tabac et de toutes les autres substances évaluées.<sup class="ref"><a href="#ref1">[1]</a></sup> Une revue de 2011 commandée pour la politique des drogues néerlandaise est parvenue à une conclusion similaire et a décrit le potentiel de préjudice physique et psychologique des champignons magiques comme faible.<sup class="ref"><a href="#ref2">[2]</a></sup> Cet article expose ce que montrent réellement les données, où se situent les risques réels et comment les réduire.</p>
        <div class="toc">
            <div class="toc-title">Sommaire</div>
            <ol>
                <li><a href="#short-answer">La réponse brève</a></li>
                <li><a href="#side-effects">Effets secondaires</a></li>
                <li><a href="#bad-trips">Mauvais trips et risque psychologique</a></li>
                <li><a href="#mental-health">Santé mentale, psychose et HPPD</a></li>
                <li><a href="#overdose">Peut-on faire une surdose ? Toxicité et empoisonnement</a></li>
                <li><a href="#emergency">Symptômes d'urgence</a></li>
                <li><a href="#interactions">Interactions médicamenteuses</a></li>
                <li><a href="#brain">Effets sur le cerveau</a></li>
                <li><a href="#who-should-avoid">Qui devrait éviter la psilocybine</a></li>
                <li><a href="#harm-reduction">Réduction des risques</a></li>
                <li><a href="#risks-benefits">Risques face aux bénéfices</a></li>
                <li><a href="#references">Références</a></li>
            </ol>
        </div>
        <h2 id="short-answer">La réponse brève</h2>
        <p>À quel point les champignons sont-ils dangereux ? Sur le plan physique, très peu. La psilocybine n'a pas de toxicité organique connue aux doses qui sont prises, ne déprime pas la respiration, et la dose estimée nécessaire pour tuer une personne est de l'ordre de mille fois une dose efficace typique.<sup class="ref"><a href="#ref3">[3]</a></sup> Aucun cas fiable de surdose mortelle par champignons à psilocybine seuls n'a été documenté chez un adulte en bonne santé ; la poignée de décès dans la littérature impliquait des espèces toxiques d'apparence similaire, une maladie cardiaque préexistante, d'autres drogues, ou des accidents comme des chutes et des noyades sous intoxication.<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup></p>
        <p>Sur le plan psychologique, le tableau est plus nuancé. Dans l'enquête la plus large sur les expériences difficiles avec la psilocybine, 39 % de près de 2 000 personnes interrogées ont classé leur pire « mauvais trip » parmi les cinq expériences les plus difficiles de leur vie, 11 % ont dit s'être mises elles-mêmes ou d'autres en risque de préjudice physique pendant l'épisode, et 7.6 % ont cherché un traitement pour des symptômes psychologiques persistants ensuite.<sup class="ref"><a href="#ref7">[7]</a></sup> La plupart de ces épisodes sont survenus sans accompagnateur sobre, dans des cadres non planifiés ou à doses élevées.</p>
        <div class="ambox">
            <strong>En résumé :</strong> le danger des champignons magiques vient surtout de <em>ce que les personnes font sous l'effet</em>, de <em>qui les prend</em> (personnes vulnérables à la psychose), de <em>ce qu'il y a d'autre dans leur organisme</em> (lithium, certaines autres drogues) et de <em>savoir si le champignon est vraiment de la psilocybine</em>. Chacun de ces risques peut être réduit de façon substantielle.
        </div>
        <h2 id="side-effects">Effets secondaires</h2>
        <p>Les effets secondaires des champignons magiques se regroupent en trois catégories : physiques, perceptifs et psychologiques. Les effets aigus commencent 20&ndash;40 minutes après l'ingestion, atteignent le maximum autour de 60&ndash;90 minutes et se résolvent en environ six heures.<sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <table class="wikitable">
            <tr><th>Type</th><th>Effets habituels</th><th>Notes</th></tr>
            <tr><td>Physiques</td><td>Nausées, vomissements (habituellement au début), dilatation pupillaire, augmentations modestes de la fréquence cardiaque et de la pression artérielle, sudation, frissons, faiblesse musculaire, mauvaise coordination, bâillements</td><td>Dans les essais contrôlés, la pression artérielle et la fréquence cardiaque montent de façon modérée et reviennent à la ligne de base en quelques heures ; les nausées sont la plainte la plus fréquente.<sup class="ref"><a href="#ref8">[8]</a></sup><sup class="ref"><a href="#ref9">[9]</a></sup></td></tr>
            <tr><td>Perceptifs</td><td>Distorsion visuelle et motifs, sens altéré du temps, synesthésie, intensification du son et de la couleur</td><td>Dépendants de la dose ; effets attendus, pas des événements indésirables en soi.</td></tr>
            <tr><td>Psychologiques</td><td>Euphorie, émerveillement, rire, ouverture émotionnelle ; aussi anxiété, peur, paranoïa, confusion, sensation de perte de contrôle</td><td>Dans une étude à dose élevée de Johns Hopkins, environ un tiers des personnes volontaires ont éprouvé une peur ou une anxiété significatives à un moment de la séance, même avec une préparation soigneuse.<sup class="ref"><a href="#ref10">[10]</a></sup></td></tr>
            <tr><td>Lendemain</td><td>Fatigue, mal de tête, humeur basse ou, à l'inverse, humeur élevée (« afterglow »)</td><td>Le mal de tête après la psilocybine est lié à la dose, commence après les effets aigus et se résout en un ou deux jours.<sup class="ref"><a href="#ref11">[11]</a></sup></td></tr>
        </table>
        <p>Une analyse groupée de 110 personnes volontaires en bonne santé dans huit études de laboratoire suisses a trouvé que la psilocybine à des doses allant jusqu'à 0.315 mg/kg n'a produit aucun préjudice perceptif, psychologique ni physique persistant chez aucune personne participante pendant le suivi.<sup class="ref"><a href="#ref9">[9]</a></sup></p>
        <h2 id="bad-trips">Mauvais trips et risque psychologique</h2>
        <p>Un « mauvais trip » est un épisode aigu d'anxiété intense, de panique, de paranoïa, de dysphorie ou de désorientation pendant les effets de la substance. C'est l'expérience indésirable grave la plus habituelle associée aux champignons magiques et le motif habituel pour lequel les personnes se présentent aux services d'urgence.<sup class="ref"><a href="#ref12">[12]</a></sup> Les mauvais trips sont fortement liés à la dose, à l'état d'esprit (« set ») et à l'environnement (« setting »).<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <p>L'enquête de 2016 de Carbonaro et ses collègues auprès de 1,993 personnes qui avaient eu un trip difficile avec la psilocybine a trouvé :<sup class="ref"><a href="#ref7">[7]</a></sup></p>
        <ul>
            <li>La dose médiane dans la pire expérience était d'environ 4 grammes de champignons séchés, approximativement une dose élevée.</li>
            <li>11 % se sont mises elles-mêmes ou d'autres personnes en risque de préjudice physique ; 2.6 % ont agi de façon agressive ou violente ; 2.7 % ont cherché une aide médicale pendant l'épisode.</li>
            <li>Trois personnes interrogées avec une anxiété, une dépression ou une idéation suicidaire préexistantes ont tenté de se suicider pendant l'expérience.</li>
            <li>7.6 % ont cherché un traitement pour des symptômes psychologiques persistants ensuite.</li>
            <li>Malgré cela, 84 % ont dit avoir bénéficié de l'expérience, et la difficulté s'associait de façon positive au sens personnel rapporté.</li>
        </ul>
        <p>Être seul, être dans un lieu inconnu ou public et prendre une dose plus élevée que prévu ont rendu le préjudice plus probable. Ce sont les variables que vise la pratique de réduction des risques.</p>
        <h2 id="mental-health">Santé mentale, psychose et HPPD</h2>
        <p>Le risque psychiatrique le plus grave est de précipiter un épisode psychotique prolongé chez quelqu'un prédisposé à des troubles psychotiques comme la schizophrénie ou le trouble bipolaire de type I. Les essais cliniques excluent ces personnes participantes, de sorte que les données prospectives sur ce groupe manquent ; l'exclusion elle-même reflète un consensus selon lequel le risque est réel.<sup class="ref"><a href="#ref13">[13]</a></sup><sup class="ref"><a href="#ref14">[14]</a></sup> Des rapports de cas décrivent une psychose, une manie et une déstabilisation de l'humeur prolongée après l'usage de champignons, habituellement chez des personnes ayant des antécédents personnels ou familiaux de ces affections.<sup class="ref"><a href="#ref14">[14]</a></sup></p>
        <p>Pour la population générale, les grandes études épidémiologiques n'ont pas trouvé que l'usage de psychédéliques élève le taux de problèmes de santé mentale. Une analyse de 130,152 adultes des États-Unis dans la National Survey on Drug Use and Health n'a trouvé aucune association entre l'usage de psychédéliques au cours de la vie (y compris la psilocybine) et le mal-être psychologique grave, le traitement de santé mentale ou les symptômes de panique, de dépression, d'anxiété ou de psychose ; certaines associations allaient dans une direction protectrice.<sup class="ref"><a href="#ref15">[15]</a></sup> Une analyse de suivi de 190,000 adultes a de même trouvé des taux plus bas de mal-être psychologique et de suicidalité au cours du mois précédent chez les personnes qui utilisaient des psychédéliques classiques.<sup class="ref"><a href="#ref16">[16]</a></sup> Ce sont des résultats corrélationnels et ils ne peuvent pas écarter le risque dans des sous-groupes vulnérables.</p>
        <p><strong>Trouble perceptif persistant induit par les hallucinogènes (HPPD)</strong>, dans lequel des altérations visuelles comme des traînées, des halos ou de la neige visuelle persistent des semaines ou des années, est un diagnostic reconnu du DSM-5. Il semble rare, s'associe plus souvent au LSD qu'à la psilocybine et n'est survenu chez aucune personne participante de la littérature moderne des essais contrôlés, bien que les enquêtes en population suggèrent que les phénomènes transitoires de « flashback » ne sont pas rares et s'estompent habituellement.<sup class="ref"><a href="#ref17">[17]</a></sup></p>
        <h2 id="overdose">Peut-on faire une surdose ? Toxicité et empoisonnement</h2>
        <p>Une « surdose » de champignons magiques au sens d'une dose toxique qui met la vie en danger n'est pas une préoccupation pratique. L'analyse comparative de Robert Gable a estimé la dose létale de psilocybine chez l'humain à environ 1,000 fois la dose efficace, contre environ 10 pour l'alcool et 6 pour l'héroïne intraveineuse.<sup class="ref"><a href="#ref3">[3]</a></sup> Les études chez l'animal situent la dose létale médiane de psilocybine autour de 280 mg/kg chez le rat, des centaines de fois la dose active humaine par kilogramme.<sup class="ref"><a href="#ref2">[2]</a></sup> Comme un champignon séché contient environ 0.5&ndash;1 % de psilocybine en poids, atteindre une quantité physiquement létale en mangeant des champignons est considéré en pratique comme impossible.<sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref4">[4]</a></sup></p>
        <p>Ce que les personnes veulent habituellement dire par « surdose », c'est prendre beaucoup plus que prévu, ce qui produit une expérience accablante et terrifiante plutôt qu'un dommage organique. Les symptômes d'une dose très élevée comprennent une confusion grave, une incapacité à communiquer, une agitation, une panique, des vomissements et, dans de rares cas, des convulsions ou une température élevée, ce dernier étant plus souvent rapporté lorsque d'autres substances étaient impliquées.<sup class="ref"><a href="#ref12">[12]</a></sup></p>
        <h3>Empoisonnement par champignons mal identifiés</h3>
        <p>Le scénario véritablement mortel impliquant des « champignons magiques » est de manger une espèce toxique par erreur. Les espèces mortelles d'<em>Amanita</em> et de <em>Galerina</em>, qui contiennent des amatoxines qui détruisent le foie, peuvent pousser dans les mêmes habitats et ressembler de façon superficielle à certaines espèces de <em>Psilocybe</em>. L'empoisonnement par amatoxines est trompeur : les symptômes gastro-intestinaux apparaissent 6&ndash;24 heures après l'ingestion, semblent s'améliorer, puis une insuffisance hépatique se développe dans les jours suivants.<sup class="ref"><a href="#ref6">[6]</a></sup> Tout champignon mangé dans la nature qui produit des vomissements et une diarrhée retardés de nombreuses heures plus tard est une urgence médicale, pas un mauvais trip.</p>
        <p>Les expositions à la psilocybine rapportées aux centres antipoison des États-Unis ont fortement augmenté au début des années 2020, avec une hausse de plus du triple chez les adolescents entre 2018 et 2022, et environ trois quarts des cas adolescents ont nécessité des soins médicaux.<sup class="ref"><a href="#ref18">[18]</a></sup> La plupart des effets rapportés étaient des hallucinations, une agitation et une tachycardie ; les issues graves étaient peu fréquentes.</p>
        <h3>Cas graves rares</h3>
        <p>Un petit nombre de rapports de cas décrivent un préjudice physique grave après l'usage de champignons, y compris une rhabdomyolyse avec lésion rénale aiguë, et un arrêt cardiaque mortel chez une personne receveuse d'une greffe cardiaque dont le cœur transplanté n'a pas pu répondre normalement aux effets autonomes de la substance.<sup class="ref"><a href="#ref5">[5]</a></sup> Les complications rénales et cardiaques s'associent plus fortement à d'autres genres de champignons (par exemple <em>Cortinarius</em>) et à des drogues co-ingérées qu'à la psilocybine elle-même.<sup class="ref"><a href="#ref4">[4]</a></sup> Ils sont documentés ici parce qu'ils existent, pas parce qu'ils sont typiques.</p>
        <h2 id="emergency">Symptômes d'urgence</h2>
        <div class="ambox warn">
            <strong>Appelez le 911 ou Poison Control (1-800-222-1222) si la personne :</strong> ne répond pas ou ne peut pas être réveillée ; a une convulsion ; a une douleur thoracique, un battement très rapide ou irrégulier, ou une difficulté à respirer ; a une température corporelle élevée avec des muscles rigides ou une sudation profuse (possible toxicité sérotoninergique, surtout si d'autres drogues sont impliquées) ; est violente, s'automutile ou tente de partir vers un lieu dangereux ; ou développe des vomissements et une diarrhée <em>des heures après</em> avoir mangé des champignons cueillis (possible empoisonnement par amatoxines).
        </div>
        <p>Une personne qui a peur, est confuse, pleure ou est convaincue que quelque chose ne va pas, mais qui est physiquement stable, n'a habituellement pas besoin d'une ambulance. Ce qui aide, c'est un accompagnateur calme, un espace calme et sûr, l'assurance que les effets sont temporaires et passeront en quelques heures, et d'éviter la contention ou la dispute.<sup class="ref"><a href="#ref19">[19]</a></sup> En cas de doute, appelez Poison Control ; le service est gratuit, confidentiel et peut conseiller si des soins hospitaliers sont nécessaires.</p>
        <h2 id="interactions">Interactions médicamenteuses</h2>
        <ul>
            <li><strong>Lithium</strong> : l'interaction documentée la plus importante. Dans une analyse de 62 rapports en ligne de psychédéliques classiques combinés avec du lithium, 47 % impliquaient des convulsions et 18 % ont nécessité des soins médicaux d'urgence ; la lamotrigine n'a pas montré ce schéma.<sup class="ref"><a href="#ref20">[20]</a></sup> La psilocybine ne doit pas être combinée avec le lithium.</li>
            <li><strong>ISRS et IRSN</strong> : les antidépresseurs atténuent habituellement les effets subjectifs de la psilocybine plutôt que de produire des effets dangereux ; le syndrome sérotoninergique par psilocybine seule n'est pas documenté, mais c'est une préoccupation théorique lorsqu'elle est combinée avec des IMAO ou du tramadol.<sup class="ref"><a href="#ref21">[21]</a></sup></li>
            <li><strong>IMAO</strong> : les inhibiteurs de la monoamine oxydase peuvent intensifier et prolonger les effets de la psilocine de façon imprévisible.<sup class="ref"><a href="#ref21">[21]</a></sup></li>
            <li><strong>Alcool et cannabis</strong> : les deux augmentent la probabilité de nausées, de confusion et d'une expérience difficile ; l'alcool ajoute un risque de blessures.<sup class="ref"><a href="#ref12">[12]</a></sup></li>
            <li><strong>Stimulants</strong> : la combinaison avec des amphétamines, de la MDMA ou de la cocaïne élève encore davantage la fréquence cardiaque et la pression artérielle et augmente le risque d'anxiété et d'hyperthermie.</li>
        </ul>
        <h2 id="brain">Effets sur le cerveau</h2>
        <p>Les effets de la psilocybine sur le cerveau sont le sujet de l'article principal du site ; ici la question est de savoir si ces effets sont nocifs. La psilocine agit surtout sur les récepteurs de la sérotonine 5-HT<sub>2A</sub>, réduit de façon transitoire l'intégrité du réseau du mode par défaut et augmente la communication entre des réseaux cérébraux habituellement séparés.<sup class="ref"><a href="#ref22">[22]</a></sup> Une étude de 2024 dans <em>Nature</em> a trouvé qu'une seule dose élevée a désynchronisé les réseaux corticaux pendant la durée des effets de la substance, avec un changement plus faible de la connexion hippocampe-réseau du mode par défaut qui a persisté des semaines.<sup class="ref"><a href="#ref23">[23]</a></sup></p>
        <p>Ces changements sont considérés comme le fondement à la fois de l'expérience aiguë et des effets thérapeutiques rapportés, et aucune étude n'a trouvé de preuve que la psilocybine endommage les neurones. Les études chez l'animal et sur cellules suggèrent le contraire : une densité accrue d'épines dendritiques et l'expression de gènes liés à la neuroplasticité.<sup class="ref"><a href="#ref24">[24]</a></sup> On ignore si ces effets de plasticité pourraient être nocifs dans un cerveau en développement ; il n'y a presque pas de données contrôlées chez les adolescents, ce qui est l'une des raisons pour lesquelles l'usage chez les jeunes est déconseillé.<sup class="ref"><a href="#ref18">[18]</a></sup></p>
        <h2 id="who-should-avoid">Qui devrait éviter la psilocybine</h2>
        <p>D'après les critères d'exclusion utilisés dans les essais cliniques et les lignes directrices de sécurité publiées :<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <ul>
            <li>Personnes ayant des antécédents personnels ou d'un parent au premier degré de schizophrénie, de trouble schizo-affectif, de trouble bipolaire de type I ou d'autres affections psychotiques.</li>
            <li>Personnes qui prennent du lithium, ou celles sous IMAO.</li>
            <li>Personnes avec une hypertension non contrôlée, un AVC ou un infarctus récent, une arythmie grave ou une autre maladie cardiovasculaire significative, en raison de l'augmentation transitoire de la pression artérielle et de la fréquence cardiaque.</li>
            <li>Personnes enceintes ou qui allaitent (pas de données de sécurité).</li>
            <li>Adolescents et enfants.</li>
            <li>Toute personne en crise aiguë, gravement intoxiquée ou sans lieu sûr et personne avec qui rester.</li>
        </ul>
        <h2 id="harm-reduction">Réduction des risques</h2>
        <p>Les mesures suivantes portent sur les sources documentées de préjudice. Elles sont tirées des lignes directrices de sécurité clinique<sup class="ref"><a href="#ref13">[13]</a></sup>, de la littérature d'enquêtes sur les expériences difficiles<sup class="ref"><a href="#ref7">[7]</a></sup> et d'organisations de réduction des risques comme le Zendo Project et DanceSafe.<sup class="ref"><a href="#ref19">[19]</a></sup></p>
        <ol>
            <li><strong>Sachez ce que vous avez.</strong> Ne mangez jamais de champignons cueillis à moins qu'une personne identifiante compétente ait confirmé l'espèce. L'identification erronée est le seul scénario le plus susceptible d'être mortel.</li>
            <li><strong>Faites un dépistage.</strong> Passez en revue les contre-indications ci-dessus avec honnêteté, y compris les antécédents familiaux et les médicaments actuels.</li>
            <li><strong>Commencez bas.</strong> La puissance varie plusieurs fois selon les espèces et même selon les lots. Une première dose de 1 gramme ou moins de <em>Psilocybe cubensis</em> séché donne une idée de l'effet ; la médiane de l'enquête pour les pires expériences était d'environ 4 grammes.</li>
            <li><strong>Ayez un accompagnateur sobre.</strong> Une personne de confiance et sobre qui peut rassurer, réorienter et demander de l'aide si besoin est la sauvegarde la plus efficace contre le préjudice pendant un mauvais trip.</li>
            <li><strong>Choisissez le cadre.</strong> Privé, familier, à l'abri de la circulation, de l'eau, des hauteurs et des machines lourdes. Ne conduisez pas. Prévoyez de rester au même endroit pendant six heures.</li>
            <li><strong>Ne mélangez pas.</strong> Surtout pas avec le lithium, l'alcool ou les stimulants.</li>
            <li><strong>Préparez-vous à la difficulté.</strong> L'anxiété et la peur sont habituelles et passent. Respirer lentement, changer de pièce, changer de musique et se faire rappeler que la substance s'estompera sont les soutiens habituels. « Fais confiance, lâche prise, ouvre-toi » est la phrase utilisée dans les séances de Johns Hopkins.<sup class="ref"><a href="#ref10">[10]</a></sup></li>
            <li><strong>Sachez quand appeler.</strong> Voir les symptômes d'urgence ci-dessus. Poison Control n'implique pas les forces de l'ordre.</li>
            <li><strong>Intégrez ensuite.</strong> Parler de l'expérience avec une personne de confiance ou un thérapeute réduit la probabilité d'un mal-être persistant.</li>
        </ol>
        <h2 id="risks-benefits">Risques face aux bénéfices</h2>
        <p>Les risques et bénéfices de la psilocybine sont de plus en plus pesés de façon formelle. Du côté du bénéfice, des essais randomisés ont rapporté de grandes réductions de la dépression,<sup class="ref"><a href="#ref25">[25]</a></sup> et des réductions de la consommation intensive d'alcool dans le trouble de l'usage d'alcool,<sup class="ref"><a href="#ref26">[26]</a></sup> habituellement après une ou deux doses supervisées. Du côté du risque, les mêmes essais rapportent une anxiété transitoire, un mal de tête, des nausées et une élévation de la pression artérielle, et très occasionnellement un mal-être prolongé. Dans des cadres supervisés avec dépistage médical, aucun essai n'a rapporté de décès, de psychose persistante ni de cas de HPPD.<sup class="ref"><a href="#ref9">[9]</a></sup><sup class="ref"><a href="#ref25">[25]</a></sup></p>
        <p>Ces résultats ne se transposent pas directement à l'usage non supervisé, où manquent le dépistage, la précision de la dose et le soutien qui produisent l'historique de sécurité. L'écart entre la sécurité clinique et le risque dans le monde réel est précisément ce que la réduction des risques tente de combler.</p>
        <h2 id="see-also">Voir aussi</h2>
        <div class="see-also">
        <ul>
            <li><a href="/fr/">Psilocybine</a> : aperçu, pharmacologie, recherche et statut juridique</li>
            <li><a href="/fr/are-shrooms-addictive/">Les champignons créent-ils une addiction ?</a> : dépendance, tolérance et potentiel d'abus</li>
            <li><a href="/fr/events/">Événements récents</a> : actualités de recherche et de politique</li>
        </ul>
        </div>
<div class="ambox help">
            <strong>Si quelqu'un a besoin d'aide maintenant :</strong> US Poison Control <strong>1-800-222-1222</strong> (24/7, gratuit, confidentiel) &middot; Urgences <strong>911</strong> &middot; Ligne de soutien par les pairs psychédélique de Fireside Project <strong>62-FIRESIDE (623-473-7433)</strong> &middot; 988 Suicide &amp; Crisis Lifeline : appelez ou envoyez un texto au <strong>988</strong>.
        </div>
        <h2 id="references">Références</h2>
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

ADDICTION_CONTENT = r"""        <h1 class="page-title">Les champignons créent-ils une addiction ?</h1>
        <p class="page-subtitle">Depuis WikiPsilocybin, l'encyclopédie libre de la psilocybine, un article de réduction des risques</p>
        <p class="hatnote">Cet article couvre la dépendance et le potentiel d'abus des champignons à psilocybine. Sur les effets secondaires, la surdose et la sécurité générale, voir <a href="/fr/are-magic-mushrooms-dangerous/">Les champignons magiques sont-ils dangereux ?</a></p>
        <div class="infobox">
            <div class="infobox-title">Potentiel d'abus de la psilocybine</div>
            <div class="infobox-row"><div class="infobox-label">Dépendance physique</div><div class="infobox-value">Non observée<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Syndrome de sevrage</div><div class="infobox-value">Aucun documenté<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Auto-administration chez l'animal</div><div class="infobox-value">Faible ou absente ; les animaux ne travaillent pas de façon fiable pour obtenir de la psilocybine<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref3">[3]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Tolérance</div><div class="infobox-value">Se développe en quelques jours ; se rétablit en grande partie après 1&ndash;2 semaines<sup class="ref"><a href="#ref4">[4]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Recommandation experte de classement</div><div class="infobox-value">Tableau IV (faible potentiel d'abus) si elle est approuvée médicalement<sup class="ref"><a href="#ref1">[1]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Classement actuel aux États-Unis</div><div class="infobox-value">Tableau I</div></div>
        </div>
        <p><strong>Les champignons à psilocybine (« champignons » ou « shrooms ») ne sont pas considérés comme addictifs de la façon dont le sont l'alcool, la nicotine, les opioïdes ou les stimulants.</strong> Ils ne produisent ni dépendance physique ni syndrome de sevrage, les animaux de laboratoire ne se les auto-administrent pas de façon fiable, et la tolérance rapide qu'ils produisent rend l'usage quotidien autolimité.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref4">[4]</a></sup> Une revue exhaustive de la psilocybine face aux huit facteurs de potentiel d'abus de la Controlled Substances Act des États-Unis a conclu que, si elle était approuvée comme médicament, elle correspondrait au Tableau IV, la catégorie des drogues à faible potentiel d'abus comme les benzodiazépines et le zolpidem, et non au Tableau I où elle se situe aujourd'hui.<sup class="ref"><a href="#ref1">[1]</a></sup></p>
        <p>Cela ne signifie pas qu'un usage problématique soit impossible. Une minorité de personnes utilise des hallucinogènes de façon assez compulsive pour remplir les critères d'un <em>trouble de l'usage d'hallucinogènes</em>, un diagnostic du DSM-5, et des habitudes psychologiques peuvent se former autour de toute expérience qu'une personne trouve significative ou évasive.<sup class="ref"><a href="#ref5">[5]</a></sup> Cet article explique la distinction, ce que disent les données et le petit nombre de situations dans lesquelles l'usage de champignons mérite attention.</p>
        <div class="toc">
            <div class="toc-title">Sommaire</div>
            <ol>
                <li><a href="#short-answer">La réponse brève</a></li>
                <li><a href="#what-addiction-means">Ce que signifie « addictif »</a></li>
                <li><a href="#evidence">Les données</a></li>
                <li><a href="#tolerance">La tolérance et pourquoi elle compte</a></li>
                <li><a href="#withdrawal">Sevrage</a></li>
                <li><a href="#use-disorder">Trouble de l'usage d'hallucinogènes</a></li>
                <li><a href="#microdosing">Le microdosage change-t-il le tableau ?</a></li>
                <li><a href="#treatment">La psilocybine comme traitement de l'addiction</a></li>
                <li><a href="#harm-reduction">Réduction des risques</a></li>
                <li><a href="#references">Références</a></li>
            </ol>
        </div>
        <h2 id="short-answer">La réponse brève</h2>
        <p>Non, selon les définitions scientifiques habituelles. Le National Institute on Drug Abuse des États-Unis affirme que la psilocybine n'est pas connue pour causer une dépendance physique, et la propre fiche de la Drug Enforcement Administration note que la psilocybine ne produit pas de conduite compulsive de recherche de drogue dans les modèles animaux.<sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref6">[6]</a></sup> Dans l'analyse multicritère de préjudice de <em>Lancet</em> de 2010, les champignons à psilocybine ont obtenu le score le plus bas de 20 drogues sur le critère de « dépendance » ainsi que sur le préjudice global.<sup class="ref"><a href="#ref7">[7]</a></sup></p>
        <p>Les traits qui rendent une drogue addictive, c'est-à-dire une activation forte de la voie de récompense dopaminergique du cerveau, un usage croissant, un sevrage physique et une envie entre les usages, sont faibles ou absents pour la psilocybine. La plupart des personnes qui essaient des champignons les utilisent une poignée de fois dans leur vie ; la National Survey on Drug Use and Health trouve de façon constante que l'usage au cours du mois précédent est une petite fraction de l'usage au cours de la vie, un schéma opposé à celui des drogues addictives.<sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <h2 id="what-addiction-means">Ce que signifie « addictif »</h2>
        <p>Les chercheurs sur l'addiction distinguent plusieurs choses auxquelles « addictif » peut renvoyer :</p>
        <ul>
            <li><strong>Dépendance physique</strong> : le corps s'adapte à la drogue de sorte que l'arrêt cause un syndrome de sevrage (alcool, opioïdes, benzodiazépines).</li>
            <li><strong>Renforcement</strong> : la drogue active directement les circuits de récompense de sorte que les animaux et les personnes travailleront pour l'obtenir de façon répétée (cocaïne, nicotine).</li>
            <li><strong>Usage compulsif</strong> : usage continu malgré le préjudice, perte de contrôle, envie ; c'est le noyau d'un trouble de l'usage de substances du DSM-5.</li>
            <li><strong>Habitude psychologique</strong> : dépendance à une expérience pour faire face ou s'évader, qui peut s'attacher à presque n'importe quelle activité.</li>
        </ul>
        <p>La psilocybine se situe bas sur les trois premiers et, comme toute expérience puissante, n'est pas à l'abri du quatrième.</p>
        <h2 id="evidence">Les données</h2>
        <h3>Études chez l'animal</h3>
        <p>Le test de laboratoire habituel du potentiel d'abus est de savoir si les animaux s'auto-administreront une drogue. Les rats et les singes s'auto-administrent facilement la cocaïne, l'héroïne, la nicotine et l'alcool. Les psychédéliques classiques, y compris la psilocybine, figurent parmi les rares drogues psychoactives que les animaux ne s'auto-administrent pas de façon fiable, et dans les tests de préférence de place conditionnée ils produisent une préférence faible ou nulle.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref3">[3]</a></sup> La psilocine n'augmente pas non plus de façon substantielle la dopamine dans le nucleus accumbens, la signature des drogues renforçantes, bien qu'elle ait des effets dopaminergiques indirects modestes.<sup class="ref"><a href="#ref3">[3]</a></sup></p>
        <h3>Études cliniques et de laboratoire chez l'humain</h3>
        <p>En plus de deux décennies d'essais cliniques modernes avec plus de mille personnes participantes ayant reçu de la psilocybine sous supervision, aucune étude n'a rapporté de recherche de drogue, d'envie ou d'usage compulsif ultérieur comme issue.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref9">[9]</a></sup> Une méta-analyse de 2024 des événements indésirables dans les essais de psychédéliques classiques n'a trouvé aucun cas de dépendance.<sup class="ref"><a href="#ref9">[9]</a></sup> Le suivi de personnes volontaires en bonne santé dans les études de Johns Hopkins a trouvé que le changement le plus habituel dans l'usage de drogues après une séance à dose élevée était une <em>baisse</em> de l'usage d'autres substances.<sup class="ref"><a href="#ref10">[10]</a></sup></p>
        <h3>Données de population</h3>
        <p>Chez les adultes des États-Unis, l'usage de psilocybine au cours de la vie est habituel (environ une personne sur dix), mais l'usage régulier est rare. Les analyses de la National Survey on Drug Use and Health n'ont trouvé aucune association entre l'usage de psychédéliques au cours de la vie et une augmentation des problèmes de santé mentale, et certaines analyses ont trouvé que l'usage de psychédéliques s'associait à des probabilités plus basses de trouble de l'usage d'opioïdes.<sup class="ref"><a href="#ref8">[8]</a></sup><sup class="ref"><a href="#ref11">[11]</a></sup></p>
        <h2 id="tolerance">La tolérance et pourquoi elle compte</h2>
        <p>La psilocybine produit une tolérance rapide et prononcée. Prendre une deuxième dose en un ou deux jours produit un effet nettement plus faible, et un dosage quotidien pendant quelques jours peut abolir l'effet psychédélique presque entièrement ; la sensibilité revient après environ une ou deux semaines d'abstinence.<sup class="ref"><a href="#ref4">[4]</a></sup> Cela vient de la régulation à la baisse des récepteurs 5-HT<sub>2A</sub> sur lesquels agit la psilocine, et s'applique de façon croisée au LSD et à la mescaline.<sup class="ref"><a href="#ref4">[4]</a></sup></p>
        <p>La tolérance rapide est l'une des principales raisons pharmacologiques pour lesquelles la psilocybine est difficile à utiliser de façon compulsive : l'usage quotidien croissant cesse simplement de fonctionner. Cela contraste nettement avec des drogues comme les opioïdes, où la tolérance pousse à des doses plus élevées plutôt que de retirer l'incitation à redoser.</p>
        <h2 id="withdrawal">Sevrage</h2>
        <p>Aucun syndrome de sevrage physique n'a été documenté pour la psilocybine chez l'humain ni chez l'animal, et elle ne figure pas parmi les substances avec un syndrome de sevrage reconnu dans le DSM-5.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup> Les personnes qui arrêtent après une période d'usage fréquent peuvent remarquer un « bas » de fatigue, d'humeur basse ou d'aplatissement pendant un ou deux jours après des séances individuelles, mais c'est un effet ultérieur de l'expérience plutôt qu'un syndrome de dépendance, et cela ne pousse pas à redoser.<sup class="ref"><a href="#ref12">[12]</a></sup></p>
        <h2 id="use-disorder">Trouble de l'usage d'hallucinogènes</h2>
        <p>Le DSM-5 inclut le « trouble de l'usage d'autres hallucinogènes » (distinct de la phencyclidine), qui peut être diagnostiqué lorsqu'une personne montre un schéma problématique d'usage, par exemple consacrer un temps excessif à obtenir ou à utiliser, abandonner des activités importantes ou continuer malgré le préjudice.<sup class="ref"><a href="#ref5">[5]</a></sup> Comme la tolérance compte comme un critère et que le sevrage ne s'applique pas, le diagnostic repose surtout sur des critères comportementaux. La prévalence est faible : le DSM-5 cite une prévalence à 12 mois d'environ 0.1 % chez les adultes des États-Unis, et dans les populations qui cherchent un traitement les hallucinogènes sont rarement la drogue principale.<sup class="ref"><a href="#ref5">[5]</a></sup><sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <p>Les signes d'alerte que l'usage est devenu problématique ressemblent à ceux de n'importe quelle substance : utiliser plus souvent que prévu, utiliser pour éviter de faire face à la vie plutôt que de s'y engager, un usage qui interfère avec le travail, les relations ou la sécurité, et une difficulté à s'arrêter malgré le souhait de le faire. Comme la psilocybine ne produit pas de dépendance physique, la réponse appropriée est le soutien psychologique plutôt que la désintoxication médicale. La National Helpline de SAMHSA (1-800-662-4357) offre des orientations gratuites et confidentielles.<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <h2 id="microdosing">Le microdosage change-t-il le tableau ?</h2>
        <p>Le microdosage, prendre des quantités subperceptuelles tous les quelques jours, est le seul schéma d'usage de psilocybine qui est habituel par conception. Même ici, aucune dépendance au sens pharmacologique n'a été observée, et la plupart des protocoles incluent des jours de pause précisément à cause de la tolérance.<sup class="ref"><a href="#ref14">[14]</a></sup> Les questions ouvertes avec le microdosage concernent l'efficacité (les études contrôlées par placebo montrent que la plupart des bénéfices rapportés sont égalés par le placebo) et l'absence de données de sécurité à long terme sur l'activation répétée des récepteurs 5-HT<sub>2B</sub>, une préoccupation théorique de valve cardiaque, plutôt que l'addiction.<sup class="ref"><a href="#ref14">[14]</a></sup><sup class="ref"><a href="#ref15">[15]</a></sup></p>
        <h2 id="treatment">La psilocybine comme traitement de l'addiction</h2>
        <p>Plutôt que de causer une addiction, la psilocybine est étudiée comme traitement de celle-ci. Dans un essai randomisé de 2022 à NYU, deux séances supervisées de psilocybine combinées à une thérapie ont réduit les jours de consommation intensive d'alcool chez des personnes avec un trouble de l'usage d'alcool de 83 % sur huit mois, contre 51 % avec un placebo actif.<sup class="ref"><a href="#ref16">[16]</a></sup> Une étude pilote de Johns Hopkins de psilocybine pour l'arrêt du tabac a rapporté 80 % d'abstinence vérifiée biologiquement à six mois et 60 % à 30 mois, bien au-dessus des taux des traitements conventionnels, bien que l'étude ait été petite et non contrôlée.<sup class="ref"><a href="#ref17">[17]</a></sup> Des essais plus larges dans les troubles de l'usage d'alcool, de tabac, d'opioïdes et de cocaïne sont en cours.</p>
        <h2 id="harm-reduction">Réduction des risques</h2>
        <p>Comme le risque d'addiction est faible, la réduction des risques pour les champignons se concentre sur les risques aigus couverts dans <a href="/fr/are-magic-mushrooms-dangerous/">Les champignons magiques sont-ils dangereux ?</a> : identification des champignons, dose, cadre, un accompagnateur sobre, et éviter les combinaisons avec le lithium, l'alcool et les stimulants. Spécifique aux schémas d'usage :</p>
        <ul>
            <li><strong>Espacez les séances.</strong> La tolérance signifie que redoser en quelques jours est en grande partie gaspillé et ajoute un effort physique sans effet. Beaucoup de personnes usagères expérimentées et de cliniciens suggèrent des semaines ou des mois entre les doses complètes.</li>
            <li><strong>Notez le motif.</strong> Utiliser pour explorer, célébrer ou traiter est différent d'utiliser pour éviter. Si les champignons sont devenus le moyen de faire face à quelque chose, ce quelque chose a encore besoin d'attention.</li>
            <li><strong>Surveillez les autres substances.</strong> Les personnes qui développent des problèmes autour des psychédéliques ont souvent un usage problématique concomitant d'alcool ou de cannabis ; ce sont habituellement les drogues à aborder en premier.</li>
            <li><strong>Les antécédents de santé mentale importent plus que le risque d'addiction.</strong> La raison principale d'être prudent avec un usage répété est la vulnérabilité psychiatrique, pas la dépendance.</li>
        </ul>
        <h2 id="see-also">Voir aussi</h2>
        <div class="see-also">
        <ul>
            <li><a href="/fr/are-magic-mushrooms-dangerous/">Les champignons magiques sont-ils dangereux ?</a> : effets secondaires, mauvais trips, surdose et interactions médicamenteuses</li>
            <li><a href="/fr/">Psilocybine</a> : aperçu, pharmacologie, recherche et statut juridique</li>
            <li><a href="/fr/#therapeutic">Applications thérapeutiques</a> : essais dans les troubles de l'usage de substances</li>
        </ul>
        </div>
<div class="ambox help">
            <strong>Si quelqu'un a besoin d'aide maintenant :</strong> US Poison Control <strong>1-800-222-1222</strong> (24/7, gratuit, confidentiel) &middot; Urgences <strong>911</strong> &middot; SAMHSA National Helpline <strong>1-800-662-4357</strong> &middot; Ligne de soutien par les pairs psychédélique de Fireside Project <strong>62-FIRESIDE (623-473-7433)</strong> &middot; 988 Suicide &amp; Crisis Lifeline : appelez ou envoyez un texto au <strong>988</strong>.
        </div>
        <h2 id="references">Références</h2>
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
            "title": "Psilocybine | WikiPsilocybin",
            "description": "WikiPsilocybin est une encyclopédie indépendante de recherche sur la psilocybine, les essais cliniques, l'actualité juridique et la réduction des risques. Chaque affirmation est citée à une source primaire.",
            "content": HOME_CONTENT,
            "extra_nav": True,
        },
        {
            "page": "/are-magic-mushrooms-dangerous/",
            "title": "Les champignons magiques sont-ils dangereux ? Risques, effets secondaires et sécurité | WikiPsilocybin",
            "description": "Les champignons magiques sont-ils dangereux ? Une revue fondée sur les preuves des risques de la psilocybine : effets secondaires, mauvais trips, surdose et symptômes d'empoisonnement, interactions médicamenteuses, contre-indications de santé mentale et réduction des risques. Entièrement référencée.",
            "content": DANGER_CONTENT,
            "extra_nav": False,
        },
        {
            "page": "/are-shrooms-addictive/",
            "title": "Les champignons créent-ils une addiction ? Dépendance, tolérance et sevrage | WikiPsilocybin",
            "description": "Les champignons créent-ils une addiction ? Ce que dit la recherche sur la dépendance à la psilocybine, la tolérance, le sevrage et le trouble de l'usage d'hallucinogènes, et pourquoi les experts jugent son potentiel d'abus faible. Entièrement référencée.",
            "content": ADDICTION_CONTENT,
            "extra_nav": False,
        },
    ]
    for spec in pages:
        html = render_page(
            lang="fr",
            page=spec["page"],
            title=spec["title"],
            description=spec["description"],
            content=spec["content"],
            active_tab="article",
            extra_nav=spec["extra_nav"],
        )
        dest = write_page("fr", spec["page"], html)
        print(f"wrote {dest}")


if __name__ == "__main__":
    main()
