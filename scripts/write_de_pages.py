#!/usr/bin/env python3
"""Write German translations of the homepage and two safety guides."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from i18n_chrome import render_page, write_page

HOME_CONTENT = r"""        <h1 class="page-title">Psilocybin</h1>
        <p class="page-subtitle">Aus WikiPsilocybin, der freien Psilocybin-Enzyklopädie, täglich aktualisiert</p>

        <div class="infobox">
            <div class="infobox-title">Psilocybin</div>
            <div class="infobox-image">
                <img src="https://d8j0ntlcm91z4.cloudfront.net/user_36uL1HV6CQZ9Ia0ikUE78jQJB98/hf_20260808_070842_c807ec80-0269-48c6-a459-06b22fa82a97.png" alt="Molekulare Visualisierung von Psilocybin">
                <div class="caption">Illustration der Konnektivität eines neuronalen Netzwerks (künstlerische Darstellung, kein Forschungsbild)</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Formel</div>
                <div class="infobox-value">C&#8321;&#8322;H&#8321;&#8327;N&#8322;O&#8324;P</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Molare Masse</div>
                <div class="infobox-value">284.25 g/mol</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Erste Isolierung</div>
                <div class="infobox-value">1958, durch Albert Hofmann</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Bekannte Arten</div>
                <div class="infobox-value">mehr als 200 Pilze</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Klinische Studien</div>
                <div class="infobox-value">mehr als 400 registriert</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Menschliche Nutzung</div>
                <div class="infobox-value">~6.000 Jahre dokumentiert</div>
            </div>
            <div class="infobox-row">
                <div class="infobox-label">Rechtslage</div>
                <div class="infobox-value">Unterschiedlich; Schedule I (US-Bundesebene), legaler therapeutischer Gebrauch in OR, CO, AU</div>
            </div>
        </div>

        <div id="recent-events" class="recent-events">
            <h3>Aktuelle Ereignisse</h3>
            <ul class="event-list">
                <li>
                    <span class="event-date">6. Aug. 2026</span>
                    <span class="event-tag tag-policy">Politik</span>
                    <span class="event-link"><a href="/events/2026-08-06-va-pivot-trial/">VA launches PIVOT, a five-site randomized trial of psilocybin for veterans with treatment-resistant depression</a></span>
                </li>
                <li>
                    <span class="event-date">30. Jul. 2026</span>
                    <span class="event-tag tag-research">Forschung</span>
                    <span class="event-link"><a href="/events/2026-07-30-osu-veterans-ptsd-pilot/">Ohio State pilot trial: 9 of 12 veterans with severe, treatment-resistant PTSD in remission one month after psilocybin-assisted therapy</a></span>
                </li>
                <li>
                    <span class="event-date">26. Jan. 2026</span>
                    <span class="event-tag tag-culture">Kultur</span>
                    <span class="event-link"><a href="/events/2026-01-26-rand-psychedelic-use-survey/">RAND survey: about 11 million US adults used psilocybin in 2025, and most past-year users microdosed</a></span>
                </li>
                <li>
                    <span class="event-date">31. März 2025</span>
                    <span class="event-tag tag-policy">Politik</span>
                    <span class="event-link"><a href="/events/2025-03-31-colorado-first-healing-center/">Colorado issues its first licensed psilocybin healing center license to The Center Origin in Denver</a></span>
                </li>
                <li>
                    <span class="event-date">17. Jul. 2024</span>
                    <span class="event-tag tag-research">Forschung</span>
                    <span class="event-link"><a href="/events/2024-07-17-washu-psilocybin-desynchronizes-brain/">Washington University study in Nature shows psilocybin desynchronizes the brain's default mode network, with some changes lasting weeks</a></span>
                </li>
            </ul>
            <span class="view-all-link"><a href="/de/events/">Alle Ereignisse anzeigen &rarr;</a></span>
        </div>

        <div class="toc">
            <div class="toc-title">Inhalt</div>
            <ol>
                <li><a href="#what-is">Was ist Psilocybin?</a></li>
                <li><a href="#how-it-works">Wirkungsweise</a></li>
                <li><a href="#research">Forschung und klinische Studien</a></li>
                <li><a href="#therapeutic">Therapeutische Anwendungen</a></li>
                <li><a href="#microdosing">Mikrodosierung</a></li>
                <li><a href="#legal">Rechtslage</a></li>
                <li><a href="#safety">Sicherheit und Schadensminderung</a></li>
            </ol>
        </div>

        <h2 id="what-is">Was ist Psilocybin?</h2>
        <p>Psilocybin ist eine natürlich vorkommende psychedelische Verbindung, die von mehr als 200 Pilzarten gebildet wird, die gewöhnlich als „Zauberpilze“ bezeichnet werden. Nach der Einnahme wandelt der Körper Psilocybin in Psilocin um, das mit Serotoninrezeptoren im Gehirn interagiert und veränderte Bewusstseinszustände, visuelle und auditive Veränderungen sowie tiefgreifende Verschiebungen von Wahrnehmung und Denken hervorruft.</p>
        <p>Erstmals isoliert und synthetisiert vom Schweizer Chemiker Albert Hofmann im Jahr 1958, wird Psilocybin seit Tausenden von Jahren in indigenen zeremoniellen Praktiken verwendet. Archäologische Befunde deuten auf eine menschliche Nutzung von Psilocybinpilzen hin, die in mesoamerikanischen Kulturen mindestens 6.000 Jahre zurückreicht.</p>

        <h2 id="how-it-works">Wirkungsweise</h2>
        <p>Psilocybin ist ein Prodrug: biologisch inaktiv, bis der Körper es metabolisiert. Nach der Einnahme entfernen alkalische Phosphatase-Enzyme im Darm und in der Leber eine Phosphatgruppe und wandeln Psilocybin in Psilocin (4-Hydroxy-N,N-Dimethyltryptamin) um.</p>
        <p>Der primäre Wirkmechanismus von Psilocin ist die Agonistwirkung an Serotonin-5-HT<sub>2A</sub>-Rezeptoren im präfrontalen Kortex. Das löst eine Kaskade von Effekten aus:</p>
        <ul>
            <li><strong>Unterbrechung des Default Mode Network (DMN)</strong>: verringert die Aktivität des „Autopilot“-Systems des Gehirns und ermöglicht die Bildung neuer neuronaler Verbindungen</li>
            <li><strong>Erhöhte neuronale Konnektivität</strong>: Hirnregionen, die gewöhnlich nicht kommunizieren, beginnen zu interagieren und erzeugen synästhetische und assoziative Erfahrungen</li>
            <li><strong>Förderung der Neuroplastizität</strong>: stimuliert dendritisches Wachstum und synaptische Dichte, insbesondere im präfrontalen Kortex und Hippocampus</li>
            <li><strong>Emotionale Verarbeitung</strong>: steigert die Reaktion der Amygdala auf emotionale Reize und verringert angstbasierte Reaktivität</li>
        </ul>
        <div class="ambox">
            <strong>Wirkdauer:</strong> Der Wirkungseintritt erfolgt in der Regel 20&ndash;40 Minuten nach der Einnahme. Die Peak-Effekte dauern 2&ndash;3 Stunden, die Gesamtdauer beträgt 4&ndash;6 Stunden. Restliche Stimmungs- und kognitive Effekte können Tage bis Wochen anhalten.
        </div>

        <h2 id="research">Forschung und klinische Studien</h2>
        <p>Das letzte Jahrzehnt hat ein beispielloses Wiederaufleben der Psilocybin-Forschung erlebt, mit bedeutenden Institutionen wie Johns Hopkins, Imperial College London, NYU und Yale, die rigorose klinische Studien durchführen.</p>

        <h3>Wichtige Meilensteine der Forschung</h3>
        <ul>
            <li><strong>2016:</strong> Johns Hopkins und NYU veröffentlichen gleichzeitig wegweisende Studien, die zeigen, dass Psilocybin substanzielle und anhaltende Rückgänge von Angst und Depression bei Krebspatienten bewirkt</li>
            <li><strong>2020:</strong> Das Johns Hopkins Center for Psychedelic &amp; Consciousness Research wird mit 17 Millionen Dollar Finanzierung gegründet</li>
            <li><strong>2021:</strong> JAMA Psychiatry veröffentlicht eine randomisierte Studie, die zeigt, dass Psilocybin-Therapie mindestens so wirksam ist wie Escitalopram (Lexapro) bei Major Depression</li>
            <li><strong>2023:</strong> Die FDA erteilt den Breakthrough-Therapy-Status für die Psilocybin-gestützte Therapie bei behandlungsresistenter Depression</li>
            <li><strong>2024&ndash;2026:</strong> Mehrere Phase-3-Studien laufen oder sind abgeschlossen zu Depression, PTBS, Abhängigkeit und Belastung am Lebensende</li>
        </ul>
        <div class="ambox">
            <strong>Aktuelle Studienzahl:</strong> Stand 2026 sind mehr als 400 registrierte klinische Studien mit Psilocybin auf ClinicalTrials.gov gelistet, die Indikationen von Major Depression über Anorexie und Clusterkopfschmerz bis zur Opioidkonsumstörung umfassen.
        </div>

        <h2 id="therapeutic">Therapeutische Anwendungen</h2>
        <p>Die Psilocybin-gestützte Therapie verbindet die pharmakologischen Wirkungen von Psilocybin mit strukturierter psychotherapeutischer Unterstützung. Die aktuelle Evidenz stützt ihr Potenzial bei der Behandlung von:</p>
        <ul>
            <li><strong>Major Depression (MDD)</strong>: Ansprechraten von 60&ndash;80% in klinischen Studien, mit Effekten, die 3&ndash;12 Monate nach 1&ndash;2 Sitzungen anhalten</li>
            <li><strong>Behandlungsresistente Depression (TRD)</strong>: Breakthrough-Therapy-Status der FDA erteilt; Phase-3-Studien laufen</li>
            <li><strong>Belastung am Lebensende</strong>: verringert existenzielle Angst und Depression bei Patientinnen und Patienten mit terminalem Krebs</li>
            <li><strong>PTBS</strong>: sich abzeichnende Evidenz aus Studien mit Veteranen zeigt eine signifikante Symptomreduktion</li>
            <li><strong>Substanzkonsumstörungen</strong>: vielversprechende Ergebnisse für Tabak- und Alkoholentwöhnung, mit Abstinenzraten, die 2&ndash;3-mal höher liegen als bei herkömmlichen Behandlungen</li>
            <li><strong>Clusterkopfschmerz</strong>: von Betroffenen berichtete Linderung und wachsende klinische Unterstützung</li>
        </ul>

        <h2 id="microdosing">Mikrodosierung</h2>
        <p>Mikrodosierung bedeutet, subperzeptuelle Dosen von Psilocybin einzunehmen: üblicherweise 50&ndash;200 mg getrocknetes Pilzmaterial, oder etwa 1/10 bis 1/20 einer vollen Dosis. Praktizierende berichten Verbesserungen von Kreativität, Konzentration, Emotionsregulation und allgemeinem Wohlbefinden, ohne psychedelische Effekte zu erleben.</p>
        <p>Obwohl anekdotische Berichte zahlreich sind, bleibt die kontrollierte Forschung zur Mikrodosierung begrenzt. Zu den bemerkenswerten Studien gehören:</p>
        <ul>
            <li>Die Selbstverblindungsstudie der Beckley Foundation von 2022, die fand, dass einige Vorteile auch in der Placebogruppe fortbestanden, was darauf hindeutet, dass Erwartungseffekte eine Rolle spielen</li>
            <li>Die Studie der University of British Columbia von 2023, die zeigte, dass Mikrodosierende bessere Stimmung und weniger Angst berichteten als Nicht-Mikrodosierende</li>
            <li>Laufende, vom NIH finanzierte Studien, die standardisierte Mikrodosierungsprotokolle zur kognitiven Stärkung und bei Stimmungsstörungen bewerten</li>
        </ul>

        <h2 id="legal">Rechtslage</h2>
        <p>Die rechtliche Landschaft für Psilocybin verändert sich weltweit rasch:</p>
        <h3>Vereinigte Staaten</h3>
        <ul>
            <li><strong>Oregon</strong>: erster Bundesstaat, der regulierte Psilocybin-Therapie legalisierte (Measure 109, 2020), mit lizenzierten Dienstleistungszentren, die seit 2023 in Betrieb sind</li>
            <li><strong>Colorado</strong>: Proposition 122 (2022) entkriminalisierte Psilocybin und schuf einen regulierten Zugangsrahmen für den therapeutischen Gebrauch</li>
            <li><strong>Kommunale Entkriminalisierung</strong>: Städte wie Denver, Oakland, Santa Cruz, Seattle, Detroit und andere haben die Strafverfolgung nachrangig gemacht</li>
            <li><strong>Bundesebene</strong>: Psilocybin bleibt Schedule I nach dem Controlled Substances Act, obwohl parteiübergreifende Gesetzgebung für Forschungsausnahmen weiter voranschreitet</li>
        </ul>

        <h3>International</h3>
        <ul>
            <li><strong>Kanada</strong>: das Special Access Program erlaubt es Angehörigen der Gesundheitsberufe, Psilocybin für behandlungsresistente Erkrankungen zu beantragen</li>
            <li><strong>Australien</strong>: die TGA ließ Psilocybin für behandlungsresistente Depression in zugelassenen psychiatrischen Settings zu (Juli 2023)</li>
            <li><strong>Jamaika und Niederlande</strong>: Psilocybin-Trüffel bzw. -Pilze über rechtliche Grauzonen oder ausdrückliche Legalität verfügbar</li>
            <li><strong>Europäische Union</strong>: mehrere Länder prüfen Regulierungsrahmen; klinische Studien expandieren in Deutschland, dem Vereinigten Königreich und der Schweiz</li>
        </ul>

        <h2 id="safety">Sicherheit und Schadensminderung</h2>
        <p class="hatnote">Hauptartikel: <a href="/de/are-magic-mushrooms-dangerous/">Sind Zauberpilze gefährlich?</a> und <a href="/de/are-shrooms-addictive/">Machen Pilze abhängig?</a></p>
        <p>Psilocybin hat im Vergleich zu anderen psychoaktiven Substanzen ein gut etabliertes Sicherheitsprofil. Die geschätzte letale Dosis liegt etwa 1.000-mal über einer typischen wirksamen Dosis, eine tödliche Überdosis durch Psilocybin allein ist bei einem gesunden Erwachsenen nicht zuverlässig dokumentiert, es erzeugt keine körperliche Abhängigkeit und keinen Entzug, und rasche Toleranz entmutigt den häufigen Gebrauch. Die multikriterielle Analyse von 2010 in <em>Lancet</em> von David Nutt und Kollegen stufte Psilocybinpilze als die am wenigsten schädlichen von 20 Freizeitdrogen ein, wenn Schaden für Konsumierende und Schaden für Dritte berücksichtigt werden.</p>
        <p>Die Risiken, die es gibt, sind vor allem psychologisch und situativ, nicht toxisch:</p>
        <ul>
            <li><strong>Bad Trips</strong>: akute Angst, Panik oder Verwirrung; in einer Umfrage zu fast 2.000 schwierigen Erfahrungen brachten 11% der Befragten sich selbst oder andere in körperliche Gefahr, und 7.6% suchten später Behandlung wegen anhaltender Symptome</li>
            <li><strong>Psychiatrische Vulnerabilität</strong>: nicht empfohlen für Personen mit persönlicher oder familiärer Vorgeschichte psychotischer Störungen oder Bipolar-I-Störung</li>
            <li><strong>Wechselwirkungen</strong>: Lithium wird mit Krampfanfällen in Verbindung gebracht, wenn es mit Psychedelika kombiniert wird; SSRI dämpfen die Effekte; MAO-Hemmer können sie verstärken</li>
            <li><strong>Kardiovaskulär</strong>: mäßige, vorübergehende Anstiege von Herzfrequenz und Blutdruck; Vorsicht bei vorbestehender Herzerkrankung</li>
            <li><strong>Verwechslung</strong>: tödliche <em>Amanita</em>- und <em>Galerina</em>-Arten können Psilocybinpilzen ähneln; gesammelte Pilze sind die Hauptquelle tödlicher „Zauberpilz“-Vergiftungen</li>
            <li><strong>Set und Setting</strong>: eine nüchterne Begleitperson, eine sichere private Umgebung und eine konservative Dosis sind die wirksamsten Schutzmaßnahmen</li>
        </ul>
        <div class="ambox">
            <strong>Brauchen Sie jetzt Hilfe?</strong> US Poison Control 1-800-222-1222 (kostenlos, vertraulich, 24/7) &middot; Fireside Project psychedelische Peer-Unterstützung 62-FIRESIDE (623-473-7433) &middot; 988 Suicide &amp; Crisis Lifeline. Für die vollständige Darstellung und die Quellen siehe <a href="/de/are-magic-mushrooms-dangerous/">Sind Zauberpilze gefährlich?</a>
        </div>
"""

DANGER_CONTENT = r"""        <h1 class="page-title">Sind Zauberpilze gefährlich?</h1>
        <p class="page-subtitle">Aus WikiPsilocybin, der freien Psilocybin-Enzyklopädie, ein Artikel zur Schadensminderung</p>
        <p class="hatnote">Dieser Artikel behandelt Risiken, Nebenwirkungen und Sicherheit von Psilocybinpilzen („Zauberpilze“ oder „Shrooms“). Zum Wirkstoff selbst siehe <a href="/de/">Psilocybin</a>. Zu Abhängigkeit und Missbrauchspotenzial siehe <a href="/de/are-shrooms-addictive/">Machen Pilze abhängig?</a></p>
        <div class="infobox">
            <div class="infobox-title">Sicherheit von Psilocybinpilzen</div>
            <div class="infobox-row"><div class="infobox-label">Körperliche Toxizität</div><div class="infobox-value">Sehr gering; das Verhältnis letale Dosis zu wirksamer Dosis wird nahe 1,000:1 geschätzt<sup class="ref"><a href="#ref3">[3]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Bestätigte Todesfälle durch Psilocybin allein</div><div class="infobox-value">Praktisch keine in der Literatur; Todesfälle betreffen falsch identifizierte giftige Pilze, Unfälle oder mit eingenommene Drogen<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Hauptrisiken</div><div class="infobox-value">Psychische Belastung („Bad Trip“), riskantes Verhalten unter der Wirkung, Psychose bei vulnerablen Personen, Wechselwirkungen, Verwechslung von Pilzen</div></div>
            <div class="infobox-row"><div class="infobox-label">Gesamtrang beim Schaden</div><div class="infobox-value">Der niedrigste von 20 Drogen in der multikriteriellen Analyse von <em>Lancet</em> 2010<sup class="ref"><a href="#ref1">[1]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Poison Control (USA)</div><div class="infobox-value">1-800-222-1222</div></div>
        </div>
        <p><strong>Zauberpilze gehören zu den körperlich am wenigsten gefährlichen untersuchten Freizeitdrogen, sind aber nicht risikofrei.</strong> Die entscheidenden Gefahren sind psychologisch, nicht toxikologisch: beängstigende oder destabilisierende Erfahrungen, Unfälle unter der Wirkung und das Auslösen einer Psychose bei Personen mit persönlicher oder familiärer Vorgeschichte psychotischer Störungen. Eine gesonderte und unterschätzte Gefahr ist, den falschen Pilz zu essen, da mehrere tödliche Arten psilocybinhaltigen ähneln.<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref6">[6]</a></sup></p>
        <p>In der multikriteriellen Analyse von <em>Lancet</em> 2010 unter Leitung von David Nutt erzielten Psilocybinpilze den niedrigsten kombinierten Schaden für Konsumierende und Dritte unter 20 Drogen, unter Cannabis, Alkohol, Tabak und jeder anderen bewerteten Substanz.<sup class="ref"><a href="#ref1">[1]</a></sup> Eine 2011 im Auftrag der niederländischen Drogenpolitik erstellte Übersicht kam zu einem ähnlichen Schluss und beschrieb das körperliche und psychische Schadenspotenzial von Zauberpilzen als gering.<sup class="ref"><a href="#ref2">[2]</a></sup> Dieser Artikel legt dar, was die Evidenz tatsächlich zeigt, wo die echten Risiken liegen und wie sie sich verringern lassen.</p>
        <div class="toc">
            <div class="toc-title">Inhalt</div>
            <ol>
                <li><a href="#short-answer">Die kurze Antwort</a></li>
                <li><a href="#side-effects">Nebenwirkungen</a></li>
                <li><a href="#bad-trips">Bad Trips und psychologisches Risiko</a></li>
                <li><a href="#mental-health">Psychische Gesundheit, Psychose und HPPD</a></li>
                <li><a href="#overdose">Kann man eine Überdosis nehmen? Toxizität und Vergiftung</a></li>
                <li><a href="#emergency">Notfalls<fim-middle>ymptome</a></li>
                <li><a href="#interactions">Wechselwirkungen</a></li>
                <li><a href="#brain">Wirkungen auf das Gehirn</a></li>
                <li><a href="#who-should-avoid">Wer sollte Psilocybin meiden</a></li>
                <li><a href="#harm-reduction">Schadensminderung</a></li>
                <li><a href="#risks-benefits">Risiken gegenüber Nutzen</a></li>
                <li><a href="#references">Quellen</a></li>
            </ol>
        </div>
        <h2 id="short-answer">Die kurze Antwort</h2>
        <p>Wie gefährlich sind Zauberpilze? Körperlich sehr wenig. Psilocybin hat bei den eingenommenen Dosen keine bekannte Organtoxizität, dämpft die Atmung nicht, und die geschätzte Dosis, die nötig wäre, um einen Menschen zu töten, liegt in der Größenordnung des Tausendfachen einer typischen wirksamen Dosis.<sup class="ref"><a href="#ref3">[3]</a></sup> Ein zuverlässiger Fall einer tödlichen Überdosis durch Psilocybinpilze allein ist bei einem gesunden Erwachsenen nicht dokumentiert; die wenigen Todesfälle in der Literatur betrafen giftige Doppelgängerarten, vorbestehende Herzerkrankung, andere Drogen oder Unfälle wie Stürze und Ertrinken unter Intoxikation.<sup class="ref"><a href="#ref4">[4]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup></p>
        <p>Psychologisch ist das Bild nuancierter. In der größten Umfrage zu schwierigen Psilocybin-Erfahrungen stuften 39% von fast 2.000 Befragten ihren schlimmsten „Bad Trip“ unter die fünf schwierigsten Erfahrungen ihres Lebens ein, 11% sagten, sie hätten sich selbst oder andere währenddessen in Gefahr körperlichen Schadens gebracht, und 7.6% suchten danach Behandlung wegen anhaltender psychischer Symptome.<sup class="ref"><a href="#ref7">[7]</a></sup> Die meisten dieser Episoden ereigneten sich ohne nüchterne Begleitperson, in ungeplanten Settings oder bei hohen Dosen.</p>
        <div class="ambox">
            <strong>Kurz gesagt:</strong> die Gefahr von Zauberpilzen kommt vor allem daher, <em>was Menschen unter der Wirkung tun</em>, <em>wer sie nimmt</em> (Personen, die für Psychose vulnerabel sind), <em>was sonst noch im Organismus ist</em> (Lithium, bestimmte andere Drogen) und <em>ob der Pilz tatsächlich Psilocybin enthält</em>. Jedes dieser Risiken lässt sich erheblich verringern.
        </div>
        <h2 id="side-effects">Nebenwirkungen</h2>
        <p>Die Nebenwirkungen von Zauberpilzen fallen in drei Gruppen: körperlich, perzeptiv und psychologisch. Akute Effekte beginnen 20&ndash;40 Minuten nach der Einnahme, erreichen den Höhepunkt um 60&ndash;90 Minuten und klingen innerhalb von etwa sechs Stunden ab.<sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <table class="wikitable">
            <tr><th>Art</th><th>Häufige Effekte</th><th>Hinweise</th></tr>
            <tr><td>Körperlich</td><td>Übelkeit, Erbrechen (meist früh), Pupillenerweiterung, mäßige Anstiege von Herzfrequenz und Blutdruck, Schwitzen, Schüttelfrost, Muskelschwäche, schlechte Koordination, Gähnen</td><td>In kontrollierten Studien steigen Blutdruck und Herzfrequenz mäßig und kehren innerhalb von Stunden zur Baseline zurück; Übelkeit ist die häufigste Beschwerde.<sup class="ref"><a href="#ref8">[8]</a></sup><sup class="ref"><a href="#ref9">[9]</a></sup></td></tr>
            <tr><td>Perzeptiv</td><td>Visuelle Verzerrung und Muster, verändertes Zeitgefühl, Synästhesie, Verstärkung von Klang und Farbe</td><td>Dosisabhängig; erwartete Effekte, keine unerwünschten Ereignisse an sich.</td></tr>
            <tr><td>Psychologisch</td><td>Euphorie, Ehrfurcht, Lachen, emotionale Offenheit; auch Angst, Furcht, Paranoia, Verwirrung, Gefühl des Kontrollverlusts</td><td>In einer Hochdosis-Studie von Johns Hopkins erlebte etwa ein Drittel der Freiwilligen irgendwann in der Sitzung erhebliche Furcht oder Angst, selbst bei sorgfältiger Vorbereitung.<sup class="ref"><a href="#ref10">[10]</a></sup></td></tr>
            <tr><td>Folgetag</td><td>Müdigkeit, Kopfschmerz, niedrige Stimmung oder umgekehrt gehobene Stimmung („Afterglow“)</td><td>Kopfschmerz nach Psilocybin ist dosisbezogen, beginnt nach den akuten Effekten und klingt innerhalb von ein oder zwei Tagen ab.<sup class="ref"><a href="#ref11">[11]</a></sup></td></tr>
        </table>
        <p>Eine gepoolte Analyse von 110 gesunden Freiwilligen in acht Schweizer Laborstudien fand, dass Psilocybin in Dosen bis 0.315 mg/kg bei keiner teilnehmenden Person im Follow-up anhaltenden perzeptiven, psychologischen oder körperlichen Schaden erzeugte.<sup class="ref"><a href="#ref9">[9]</a></sup></p>
        <h2 id="bad-trips">Bad Trips und psychologisches Risiko</h2>
        <p>Ein „Bad Trip“ ist eine akute Episode intensiver Angst, Panik, Paranoia, Dysphorie oder Desorientierung während der Substanzwirkung. Es ist die häufigste schwerwiegende unerwünschte Erfahrung im Zusammenhang mit Zauberpilzen und der übliche Grund, warum Menschen Notaufnahmen aufsuchen.<sup class="ref"><a href="#ref12">[12]</a></sup> Bad Trips sind stark an Dosis, mentale Verfassung („Set“) und Umgebung („Setting“) gebunden.<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <p>Die Umfrage von Carbonaro und Kollegen aus dem Jahr 2016 unter 1,993 Personen, die einen schwierigen Psilocybin-Trip erlebt hatten, fand:<sup class="ref"><a href="#ref7">[7]</a></sup></p>
        <ul>
            <li>Die mediane Dosis in der schlechtesten Erfahrung lag bei etwa 4 Gramm getrockneter Pilze, ungefähr einer hohen Dosis.</li>
            <li>11% brachten sich selbst oder andere in Gefahr körperlichen Schadens; 2.6% handelten aggressiv oder gewalttätig; 2.7% suchten während der Episode medizinische Hilfe.</li>
            <li>Drei Befragte mit vorbestehender Angst, Depression oder Suizidgedanken versuchten während der Erfahrung Suizid.</li>
            <li>7.6% suchten danach Behandlung wegen anhaltender psychischer Symptome.</li>
            <li>Trotz dessen sagten 84%, sie hätten von der Erfahrung profitiert, und die Schwierigkeit war positiv mit der berichteten persönlichen Bedeutung assoziiert.</li>
        </ul>
        <p>Alleinsein, ein unbekannter oder öffentlicher Ort und eine größere Dosis als beabsichtigt machten Schaden wahrscheinlicher. Das sind die Variablen, auf die die Praxis der Schadensminderung zielt.</p>
        <h2 id="mental-health">Psychische Gesundheit, Psychose und HPPD</h2>
        <p>Das schwerwiegendste psychiatrische Risiko ist, bei jemandem mit Veranlagung zu psychotischen Störungen wie Schizophrenie oder Bipolar-I-Störung eine anhaltende psychotische Episode auszulösen. Klinische Studien schließen solche Teilnehmenden aus, sodass prospektive Daten zu dieser Gruppe fehlen; der Ausschluss selbst spiegelt den Konsens wider, dass das Risiko real ist.<sup class="ref"><a href="#ref13">[13]</a></sup><sup class="ref"><a href="#ref14">[14]</a></sup> Fallberichte beschreiben Psychose, Manie und anhaltende Stimmungsdestabilisierung nach Pilzkonsum, gewöhnlich bei Personen mit persönlicher oder familiärer Vorgeschichte dieser Erkrankungen.<sup class="ref"><a href="#ref14">[14]</a></sup></p>
        <p>Für die Allgemeinbevölkerung haben große epidemiologische Studien nicht gefunden, dass Psychedelika-Konsum die Rate psychischer Probleme erhöht. Eine Analyse von 130,152 Erwachsenen in den USA in der National Survey on Drug Use and Health fand keine Assoziation zwischen lebenslangem Psychedelika-Konsum (einschließlich Psilocybin) und schwerer psychischer Belastung, Behandlung psychischer Gesundheit oder Symptomen von Panik, Depression, Angst oder Psychose; einige Assoziationen liefen in schützende Richtung.<sup class="ref"><a href="#ref15">[15]</a></sup> Eine Follow-up-Analyse von 190,000 Erwachsenen fand ähnlich niedrigere Raten psychischer Belastung und Suizidalität im Vormonat unter Konsumierenden klassischer Psychedelika.<sup class="ref"><a href="#ref16">[16]</a></sup> Das sind korrelative Befunde und können Risiko in vulnerablen Untergruppen nicht ausschließen.</p>
        <p><strong>Anhaltende Wahrnehmungsstörung nach Halluzinogenen (HPPD)</strong>, bei der visuelle Störungen wie Nachzieheffekte, Höfe oder visuelles Schnee-Phänomen Wochen oder Jahre anhalten, ist eine anerkannte DSM-5-Diagnose. Sie scheint selten zu sein, wird häufiger mit LSD als mit Psilocybin in Verbindung gebracht und trat bei keiner teilnehmenden Person in der modernen kontrollierten Studienliteratur auf, obwohl Bevölkerungsbefragungen nahelegen, dass vorübergehende „Flashback“-Phänomene nicht ungewöhnlich sind und gewöhnlich verblassen.<sup class="ref"><a href="#ref17">[17]</a></sup></p>
        <h2 id="overdose">Kann man eine Überdosis nehmen? Toxizität und Vergiftung</h2>
        <p>Eine „Überdosis“ von Zauberpilzen im Sinne einer lebensbedrohlichen toxischen Dosis ist kein praktisches Problem. Die vergleichende Analyse von Robert Gable schätzte die letale Dosis von Psilocybin beim Menschen auf etwa das 1,000-Fache der wirksamen Dosis, gegenüber etwa 10 für Alkohol und 6 für intravenöses Heroin.<sup class="ref"><a href="#ref3">[3]</a></sup> Tierstudien setzen die mittlere letale Dosis von Psilocybin bei etwa 280 mg/kg bei Ratten an, dem Hundertfachen der aktiven Humandosis pro Kilogramm.<sup class="ref"><a href="#ref2">[2]</a></sup> Weil ein getrockneter Pilz etwa 0.5&ndash;1% Psilocybin nach Gewicht enthält, gilt das Erreichen einer körperlich letalen Menge durch das Essen von Pilzen als praktisch unmöglich.<sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref4">[4]</a></sup></p>
        <p>Was Menschen gewöhnlich mit „Überdosis“ meinen, ist, weit mehr als beabsichtigt zu nehmen, was eine überwältigende, beängstigende Erfahrung erzeugt, nicht Organschaden. Symptome einer sehr hohen Dosis umfassen schwere Verwirrung, Unfähigkeit zu kommunizieren, Agitation, Panik, Erbrechen und in seltenen Fällen Krampfanfälle oder hohe Temperatur, Letzteres am häufigsten berichtet, wenn andere Substanzen beteiligt waren.<sup class="ref"><a href="#ref12">[12]</a></sup></p>
        <h3>Vergiftung durch falsch identifizierte Pilze</h3>
        <p>Das wirklich tödliche Szenario im Zusammenhang mit „Zauberpilzen“ ist, irrtümlich eine giftige Art zu essen. Tödliche <em>Amanita</em>- und <em>Galerina</em>-Arten, die leberschädigende Amatoxine enthalten, können in denselben Habitaten wachsen und einigen <em>Psilocybe</em>-Arten oberflächlich ähneln. Amatoxin-Vergiftung ist täuschend: Magen-Darm-Symptome treten 6&ndash;24 Stunden nach der Einnahme auf, scheinen sich zu bessern, und dann entwickelt sich in den folgenden Tagen Leberversagen.<sup class="ref"><a href="#ref6">[6]</a></sup> Jeder in der Natur gegessene Pilz, der viele Stunden später verzögertes Erbrechen und Durchfall erzeugt, ist ein medizinischer Notfall, kein Bad Trip.</p>
        <p>An US-Giftnotrufzentralen gemeldete Psilocybin-Expositionen stiegen Anfang der 2020er Jahre stark an, mit einem mehr als dreifachen Anstieg unter Jugendlichen zwischen 2018 und 2022, und etwa drei Viertel der Fälle bei Jugendlichen erforderten medizinische Versorgung.<sup class="ref"><a href="#ref18">[18]</a></sup> Die meisten berichteten Effekte waren Halluzinationen, Agitation und Tachykardie; schwere Verläufe waren selten.</p>
        <h3>Seltene schwere Fälle</h3>
        <p>Eine kleine Zahl von Fallberichten beschreibt schweren körperlichen Schaden nach Pilzkonsum, darunter Rhabdomyolyse mit akuter Nierenschädigung und einen tödlichen Herzstillstand bei einer herztransplantierten Person, deren transplantiertes Herz nicht normal auf die autonomen Effekte der Substanz reagieren konnte.<sup class="ref"><a href="#ref5">[5]</a></sup> Nieren- und Herzkomplikationen sind stärker mit anderen Pilzgattungen (zum Beispiel <em>Cortinarius</em>) und mit mit eingenommenen Drogen assoziiert als mit Psilocybin selbst.<sup class="ref"><a href="#ref4">[4]</a></sup> Sie werden hier dokumentiert, weil sie existieren, nicht weil sie typisch sind.</p>
        <h2 id="emergency">Notfallsymptome</h2>
        <div class="ambox warn">
            <strong>Rufen Sie 911 oder Poison Control (1-800-222-1222) an, wenn die Person:</strong> nicht reagiert oder nicht geweckt werden kann; einen Krampfanfall hat; Brustschmerz, einen sehr schnellen oder unregelmäßigen Herzschlag oder Atemnot hat; eine hohe Körpertemperatur mit starren Muskeln oder profusem Schwitzen hat (mögliche serotonerge Toxizität, besonders wenn andere Drogen beteiligt sind); gewalttätig ist, sich selbst verletzt oder versucht, an einen gefährlichen Ort zu gehen; oder Erbrechen und Durchfall <em>Stunden nach</em> dem Essen gesammelter Pilze entwickelt (mögliche Amatoxin-Vergiftung).
        </div>
        <p>Eine Person, die ängstlich, verwirrt, weinend oder überzeugt ist, dass etwas nicht stimmt, aber körperlich stabil ist, braucht in der Regel keinen Krankenwagen. Was hilft, ist eine ruhige Begleitperson, ein stiller sicherer Raum, die Beruhigung, dass die Effekte vorübergehend sind und in ein paar Stunden nachlassen, und das Vermeiden von Fixierung oder Streit.<sup class="ref"><a href="#ref19">[19]</a></sup> Im Zweifel rufen Sie Poison Control an; der Dienst ist kostenlos, vertraulich und kann beraten, ob Krankenhausversorgung nötig ist.</p>
        <h2 id="interactions">Wechselwirkungen</h2>
        <ul>
            <li><strong>Lithium</strong>: die wichtigste dokumentierte Wechselwirkung. In einer Analyse von 62 Online-Berichten klassischer Psychedelika kombiniert mit Lithium betrafen 47% Krampfanfälle und 18% erforderten notfallmedizinische Versorgung; Lamotrigin zeigte kein solches Muster.<sup class="ref"><a href="#ref20">[20]</a></sup> Psilocybin sollte nicht mit Lithium kombiniert werden.</li>
            <li><strong>SSRI und SNRI</strong>: Antidepressiva dämpfen eher die subjektiven Effekte von Psilocybin, als gefährliche zu erzeugen; ein Serotoninsyndrom durch Psilocybin allein ist nicht dokumentiert, ist aber ein theoretisches Anliegen in Kombination mit MAO-Hemmern oder Tramadol.<sup class="ref"><a href="#ref21">[21]</a></sup></li>
            <li><strong>MAO-Hemmer</strong>: Monoaminooxidase-Hemmer können die Effekte von Psilocin unvorhersehbar verstärken und verlängern.<sup class="ref"><a href="#ref21">[21]</a></sup></li>
            <li><strong>Alkohol und Cannabis</strong>: beide erhöhen die Wahrscheinlichkeit von Übelkeit, Verwirrung und einer schwierigen Erfahrung; Alkohol erhöht das Verletzungsrisiko.<sup class="ref"><a href="#ref12">[12]</a></sup></li>
            <li><strong>Stimulanzien</strong>: die Kombination mit Amphetaminen, MDMA oder Kokain hebt Herzfrequenz und Blutdruck weiter an und erhöht das Risiko von Angst und Hyperthermie.</li>
        </ul>
        <h2 id="brain">Wirkungen auf das Gehirn</h2>
        <p>Die Wirkungen von Psilocybin auf das Gehirn sind das Thema des Hauptartikels der Website; hier ist die Frage, ob diese Wirkungen schädlich sind. Psilocin wirkt vor allem an Serotonin-5-HT<sub>2A</sub>-Rezeptoren, verringert vorübergehend die Integrität des Default Mode Network und erhöht die Kommunikation zwischen Hirnnetzwerken, die gewöhnlich getrennt sind.<sup class="ref"><a href="#ref22">[22]</a></sup> Eine Studie von 2024 in <em>Nature</em> fand, dass eine einzelne hohe Dosis kortikale Netzwerke für die Dauer der Substanzwirkung desynchronisierte, mit einer kleineren Veränderung der Verbindung Hippocampus–Default-Mode, die Wochen anhielt.<sup class="ref"><a href="#ref23">[23]</a></sup></p>
        <p>Diese Veränderungen gelten als Grundlage sowohl der akuten Erfahrung als auch der berichteten therapeutischen Effekte, und keine Studie hat Evidenz gefunden, dass Psilocybin Neuronen schädigt. Tier- und Zellstudien legen das Gegenteil nahe: erhöhte Dichte dendritischer Dornen und Expression von Genen, die mit Neuroplastizität zusammenhängen.<sup class="ref"><a href="#ref24">[24]</a></sup> Ob diese Plastizitätseffekte in einem sich entwickelnden Gehirn schädlich sein könnten, ist unbekannt; kontrollierte Daten bei Jugendlichen gibt es fast nicht, was einer der Gründe ist, warum der Gebrauch bei jungen Menschen abgeraten wird.<sup class="ref"><a href="#ref18">[18]</a></sup></p>
        <h2 id="who-should-avoid">Wer sollte Psilocybin meiden</h2>
        <p>Ausgehend von den Ausschlusskriterien klinischer Studien und veröffentlichten Sicherheitsleitlinien:<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <ul>
            <li>Personen mit persönlicher oder erstgradiger familiärer Vorgeschichte von Schizophrenie, schizoaffektiver Störung, Bipolar-I-Störung oder anderen psychotischen Erkrankungen.</li>
            <li>Personen, die Lithium einnehmen, oder die MAO-Hemmer nehmen.</li>
            <li>Personen mit unkontrolliertem Bluthochdruck, kürzlichem Schlaganfall oder Herzinfarkt, schwerer Arrhythmie oder anderer signifikanter Herz-Kreislauf-Erkrankung, wegen des vorübergehenden Anstiegs von Blutdruck und Herzfrequenz.</li>
            <li>Personen, die schwanger sind oder stillen (keine Sicherheitsdaten).</li>
            <li>Jugendliche und Kinder.</li>
            <li>Jede Person, die sich in einer akuten Krise befindet, schwer intoxikiert ist oder keinen sicheren Ort und keine Begleitperson hat.</li>
        </ul>
        <h2 id="harm-reduction">Schadensminderung</h2>
        <p>Die folgenden Maßnahmen richten sich an die dokumentierten Schadensquellen. Sie stammen aus klinischen Sicherheitsleitlinien<sup class="ref"><a href="#ref13">[13]</a></sup>, der Umfrageliteratur zu schwierigen Erfahrungen<sup class="ref"><a href="#ref7">[7]</a></sup> und Organisationen der Schadensminderung wie dem Zendo Project und DanceSafe.<sup class="ref"><a href="#ref19">[19]</a></sup></p>
        <ol>
            <li><strong>Wissen Sie, was Sie haben.</strong> Essen Sie niemals gesammelte Pilze, es sei denn, eine kompetente bestimmende Person hat die Art bestätigt. Verwechslung ist das einzige Szenario, das am ehesten tödlich sein kann.</li>
            <li><strong>Prüfen Sie sich selbst.</strong> Gehen Sie die Kontraindikationen oben ehrlich durch, einschließlich Familiengeschichte und aktueller Medikamente.</li>
            <li><strong>Beginnen Sie niedrig.</strong> Die Potenz variiert um ein Mehrfaches zwischen Arten und sogar zwischen Chargen. Eine erste Dosis von 1 Gramm oder weniger getrocknetem <em>Psilocybe cubensis</em> gibt ein Gefühl für die Wirkung; der Umfrage-Median für die schlechtesten Erfahrungen lag bei etwa 4 Gramm.</li>
            <li><strong>Haben Sie eine nüchterne Begleitperson.</strong> Eine vertrauenswürdige, nüchterne Person, die beruhigen, umlenken und bei Bedarf Hilfe holen kann, ist die wirksamste Schutzmaßnahme gegen Schaden während eines Bad Trips.</li>
            <li><strong>Wählen Sie das Setting.</strong> Privat, vertraut, sicher vor Verkehr, Wasser, Höhen und schwerer Maschinerie. Fahren Sie nicht. Planen Sie, sechs Stunden am selben Ort zu bleiben.</li>
            <li><strong>Nicht mischen.</strong> Besonders nicht mit Lithium, Alkohol oder Stimulanzien.</li>
            <li><strong>Bereiten Sie sich auf Schwierigkeit vor.</strong> Angst und Furcht sind häufig und gehen vorüber. Langsames Atmen, den Raum wechseln, die Musik wechseln und daran erinnert zu werden, dass die Substanz nachlässt, sind die üblichen Stützen. „Vertraue, lass los, sei offen“ ist der Satz, der in Johns-Hopkins-Sitzungen verwendet wird.<sup class="ref"><a href="#ref10">[10]</a></sup></li>
            <li><strong>Wissen Sie, wann Sie anrufen.</strong> Siehe die Notfallsymptome oben. Poison Control schaltet die Strafverfolgung nicht ein.</li>
            <li><strong>Integrieren Sie danach.</strong> Über die Erfahrung mit einer vertrauenswürdigen Person oder einer therapeutischen Fachkraft zu sprechen, verringert die Wahrscheinlichkeit anhaltender Belastung.</li>
        </ol>
        <h2 id="risks-benefits">Risiken gegenüber Nutzen</h2>
        <p>Risiken und Nutzen von Psilocybin werden zunehmend formal abgewogen. Auf der Nutzenseite haben randomisierte Studien große Rückgänge der Depression berichtet,<sup class="ref"><a href="#ref25">[25]</a></sup> und Rückgänge des starken Alkoholkonsums bei Alkoholkonsumstörung,<sup class="ref"><a href="#ref26">[26]</a></sup> gewöhnlich nach ein oder zwei überwachten Dosen. Auf der Risikoseite berichten dieselben Studien vorübergehende Angst, Kopfschmerz, Übelkeit und Blutdruckanstieg und sehr gelegentlich anhaltende Belastung. In überwachten Settings mit medizinischem Screening hat keine Studie einen Todesfall, eine anhaltende Psychose oder einen Fall von HPPD berichtet.<sup class="ref"><a href="#ref9">[9]</a></sup><sup class="ref"><a href="#ref25">[25]</a></sup></p>
        <p>Diese Ergebnisse übertragen sich nicht direkt auf den nicht überwachten Gebrauch, bei dem das Screening, die Dosierungsgenauigkeit und die Unterstützung fehlen, die die Sicherheitsbilanz erzeugen. Die Lücke zwischen klinischer Sicherheit und Risiko in der realen Welt ist genau das, was Schadensminderung zu schließen versucht.</p>
        <h2 id="see-also">Siehe auch</h2>
        <div class="see-also">
        <ul>
            <li><a href="/de/">Psilocybin</a>: Überblick, Pharmakologie, Forschung und Rechtslage</li>
            <li><a href="/de/are-shrooms-addictive/">Machen Pilze abhängig?</a>: Abhängigkeit, Toleranz und Missbrauchspotenzial</li>
            <li><a href="/de/events/">Aktuelle Ereignisse</a>: Nachrichten zu Forschung und Politik</li>
        </ul>
        </div>
<div class="ambox help">
            <strong>Wenn jemand jetzt Hilfe braucht:</strong> US Poison Control <strong>1-800-222-1222</strong> (24/7, kostenlos, vertraulich) &middot; Notruf <strong>911</strong> &middot; Psychedelische Peer-Unterstützungshotline von Fireside Project <strong>62-FIRESIDE (623-473-7433)</strong> &middot; 988 Suicide &amp; Crisis Lifeline: anrufen oder eine Nachricht senden an <strong>988</strong>.
        </div>
        <h2 id="references">Quellen</h2>
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

ADDICTION_CONTENT = r"""        <h1 class="page-title">Machen Pilze abhängig?</h1>
        <p class="page-subtitle">Aus WikiPsilocybin, der freien Psilocybin-Enzyklopädie, ein Artikel zur Schadensminderung</p>
        <p class="hatnote">Dieser Artikel behandelt Abhängigkeit und Missbrauchspotenzial von Psilocybinpilzen. Zu Nebenwirkungen, Überdosis und allgemeiner Sicherheit siehe <a href="/de/are-magic-mushrooms-dangerous/">Sind Zauberpilze gefährlich?</a></p>
        <div class="infobox">
            <div class="infobox-title">Missbrauchspotenzial von Psilocybin</div>
            <div class="infobox-row"><div class="infobox-label">Körperliche Abhängigkeit</div><div class="infobox-value">Nicht beobachtet<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Entzugssyndrom</div><div class="infobox-value">Keines dokumentiert<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Selbstverabreichung bei Tieren</div><div class="infobox-value">Schwach oder fehlend; Tiere arbeiten nicht zuverlässig für Psilocybin<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref3">[3]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Toleranz</div><div class="infobox-value">Entwickelt sich innerhalb von Tagen; setzt sich nach 1&ndash;2 Wochen weitgehend zurück<sup class="ref"><a href="#ref4">[4]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Fachliche Einordnungsempfehlung</div><div class="infobox-value">Schedule IV (geringes Missbrauchspotenzial), wenn medizinisch zugelassen<sup class="ref"><a href="#ref1">[1]</a></sup></div></div>
            <div class="infobox-row"><div class="infobox-label">Aktuelle US-Einordnung</div><div class="infobox-value">Schedule I</div></div>
        </div>
        <p><strong>Psilocybinpilze („Zauberpilze“ oder „Shrooms“) gelten nicht als abhängig machend in der Weise, wie es Alkohol, Nikotin, Opioide oder Stimulanzien sind.</strong> Sie erzeugen keine körperliche Abhängigkeit und kein Entzugssyndrom, Labortiere verabreichen sie sich nicht zuverlässig selbst, und die rasche Toleranz, die sie erzeugen, begrenzt den täglichen Gebrauch von selbst.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref4">[4]</a></sup> Eine umfassende Prüfung von Psilocybin anhand der acht Faktoren des Missbrauchspotenzials des US Controlled Substances Act kam zu dem Schluss, dass es bei Zulassung als Arzneimittel in Schedule IV passen würde, die Kategorie für Drogen mit geringem Missbrauchspotenzial wie Benzodiazepine und Zolpidem, und nicht in Schedule I, wo es jetzt steht.<sup class="ref"><a href="#ref1">[1]</a></sup></p>
        <p>Das bedeutet nicht, dass problematischer Gebrauch unmöglich ist. Eine Minderheit der Menschen konsumiert Halluzinogene so zwanghaft, dass die Kriterien für eine <em>Halluzinogenkonsumstörung</em> erfüllt sind, eine Diagnose im DSM-5, und psychologische Gewohnheiten können sich um jede Erfahrung bilden, die eine Person als bedeutsam oder als Flucht empfindet.<sup class="ref"><a href="#ref5">[5]</a></sup> Dieser Artikel erklärt die Unterscheidung, was die Evidenz sagt, und die kleine Zahl von Situationen, in denen der Gebrauch von Pilzen Aufmerksamkeit verdient.</p>
        <div class="toc">
            <div class="toc-title">Inhalt</div>
            <ol>
                <li><a href="#short-answer">Die kurze Antwort</a></li>
                <li><a href="#what-addiction-means">Was „abhängig machend“ bedeutet</a></li>
                <li><a href="#evidence">Die Evidenz</a></li>
                <li><a href="#tolerance">Die Toleranz und warum sie wichtig ist</a></li>
                <li><a href="#withdrawal">Entzug</a></li>
                <li><a href="#use-disorder">Halluzinogenkonsumstörung</a></li>
                <li><a href="#microdosing">Verändert Mikrodosierung das Bild?</a></li>
                <li><a href="#treatment">Psilocybin als Behandlung der Abhängigkeit</a></li>
                <li><a href="#harm-reduction">Schadensminderung</a></li>
                <li><a href="#references">Quellen</a></li>
            </ol>
        </div>
        <h2 id="short-answer">Die kurze Antwort</h2>
        <p>Nein, nach den üblichen wissenschaftlichen Definitionen. Das US National Institute on Drug Abuse stellt fest, dass von Psilocybin nicht bekannt ist, dass es körperliche Abhängigkeit verursacht, und das eigene Faktenblatt der Drug Enforcement Administration merkt an, dass Psilocybin in Tiermodellen kein zwanghaftes Drogensuchverhalten erzeugt.<sup class="ref"><a href="#ref2">[2]</a></sup><sup class="ref"><a href="#ref6">[6]</a></sup> In der multikriteriellen Schadensanalyse von <em>Lancet</em> 2010 erzielten Psilocybinpilze den niedrigsten Wert von 20 Drogen beim Kriterium „Abhängigkeit“ und auch beim Gesamtschaden.<sup class="ref"><a href="#ref7">[7]</a></sup></p>
        <p>Die Merkmale, die eine Droge abhängig machen, also eine starke Aktivierung der dopaminergen Belohnungsbahn des Gehirns, steigender Gebrauch, körperlicher Entzug und Verlangen zwischen den Einnahmen, sind bei Psilocybin schwach oder fehlen. Die meisten Menschen, die Pilze ausprobieren, nehmen sie ein paar Mal im Leben; die National Survey on Drug Use and Health findet durchgängig, dass der Konsum im Vormonat ein kleiner Bruchteil des lebenslangen Konsums ist, ein Muster, das dem abhängiger Drogen entgegengesetzt ist.<sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <h2 id="what-addiction-means">Was „abhängig machend“ bedeutet</h2>
        <p>Forschende zur Abhängigkeit unterscheiden mehrere Dinge, auf die sich „abhängig machend“ beziehen kann:</p>
        <ul>
            <li><strong>Körperliche Abhängigkeit</strong>: der Körper passt sich an die Droge an, sodass das Absetzen ein Entzugssyndrom verursacht (Alkohol, Opioide, Benzodiazepine).</li>
            <li><strong>Verstärkung</strong>: die Droge aktiviert direkt Belohnungskreise, sodass Tiere und Menschen wiederholt dafür arbeiten, sie zu erhalten (Kokain, Nikotin).</li>
            <li><strong>Zwanghafter Gebrauch</strong>: fortgesetzter Gebrauch trotz Schaden, Kontrollverlust, Verlangen; das ist der Kern einer Substanzkonsumstörung nach DSM-5.</li>
            <li><strong>Psychologische Gewohnheit</strong>: Angewiesenheit auf eine Erfahrung zur Bewältigung oder Flucht, die sich an fast jede Tätigkeit heften kann.</li>
        </ul>
        <p>Psilocybin liegt bei den ersten dreien niedrig und ist, wie jede starke Erfahrung, gegen das vierte nicht immun.</p>
        <h2 id="evidence">Die Evidenz</h2>
        <h3>Tierstudien</h3>
        <p>Der übliche Labortest des Missbrauchspotenzials ist, ob sich Tiere eine Droge selbst verabreichen. Ratten und Affen verabreichen sich leicht Kokain, Heroin, Nikotin und Alkohol. Klassische Psychedelika, einschließlich Psilocybin, gehören zu den wenigen psychoaktiven Drogen, die sich Tiere nicht zuverlässig selbst verabreichen, und in Tests der konditionierten Ortspräferenz erzeugen sie schwache oder keine Präferenz.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref3">[3]</a></sup> Psilocin erhöht auch nicht wesentlich Dopamin im Nucleus accumbens, der Signatur verstärkender Drogen, obwohl es bescheidene indirekte dopaminerge Effekte hat.<sup class="ref"><a href="#ref3">[3]</a></sup></p>
        <h3>Klinische und Laborstudien am Menschen</h3>
        <p>In mehr als zwei Jahrzehnten moderner klinischer Studien mit mehr als tausend Teilnehmenden, die Psilocybin unter Aufsicht erhielten, hat keine Studie Drogensuche, Verlangen oder späteren zwanghaften Gebrauch als Ergebnis berichtet.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref9">[9]</a></sup> Eine Metaanalyse von 2024 zu unerwünschten Ereignissen in Studien zu klassischen Psychedelika fand keine Fälle von Abhängigkeit.<sup class="ref"><a href="#ref9">[9]</a></sup> Das Follow-up gesunder Freiwilliger in den Johns-Hopkins-Studien fand, dass die häufigste Veränderung im Drogenkonsum nach einer Hochdosis-Sitzung ein <em>Rückgang</em> des Konsums anderer Substanzen war.<sup class="ref"><a href="#ref10">[10]</a></sup></p>
        <h3>Bevölkerungsdaten</h3>
        <p>Unter Erwachsenen in den USA ist lebenslanger Psilocybin-Konsum häufig (etwa einer von zehn), regelmäßiger Konsum aber selten. Analysen der National Survey on Drug Use and Health fanden keine Assoziation zwischen lebenslangem Psychedelika-Konsum und einem Anstieg psychischer Probleme, und einige Analysen fanden, dass Psychedelika-Konsum mit geringeren Odds einer Opioidkonsumstörung assoziiert war.<sup class="ref"><a href="#ref8">[8]</a></sup><sup class="ref"><a href="#ref11">[11]</a></sup></p>
        <h2 id="tolerance">Die Toleranz und warum sie wichtig ist</h2>
        <p>Psilocybin erzeugt eine rasche und ausgeprägte Toleranz. Eine zweite Dosis innerhalb von ein oder zwei Tagen erzeugt einen deutlich schwächeren Effekt, und tägliche Dosierung über wenige Tage kann den psychedelischen Effekt nahezu vollständig aufheben; die Empfindlichkeit kehrt nach etwa ein bis zwei Wochen Abstinenz zurück.<sup class="ref"><a href="#ref4">[4]</a></sup> Das liegt an der Herunterregulation der 5-HT<sub>2A</sub>-Rezeptoren, an denen Psilocin wirkt, und gilt kreuzweise auch für LSD und Meskalin.<sup class="ref"><a href="#ref4">[4]</a></sup></p>
        <p>Rasche Toleranz ist einer der wichtigsten pharmakologischen Gründe, warum Psilocybin schwer zwanghaft zu gebrauchen ist: steigender täglicher Gebrauch funktioniert einfach nicht mehr. Das steht im scharfen Gegensatz zu Drogen wie Opioiden, bei denen Toleranz höhere Dosen antreibt, statt den Anreiz zur erneuten Einnahme zu nehmen.</p>
        <h2 id="withdrawal">Entzug</h2>
        <p>Ein körperliches Entzugssyndrom ist für Psilocybin weder bei Menschen noch bei Tieren dokumentiert, und es steht nicht unter den Substanzen mit einem anerkannten Entzugssyndrom im DSM-5.<sup class="ref"><a href="#ref1">[1]</a></sup><sup class="ref"><a href="#ref5">[5]</a></sup> Wer nach einer Phase häufigen Gebrauchs aufhört, kann einen „Abschwung“ aus Müdigkeit, niedriger Stimmung oder Abflachung für ein oder zwei Tage nach einzelnen Sitzungen bemerken, aber das ist eine Nachwirkung der Erfahrung, kein Abhängigkeitssyndrom, und es treibt keine erneute Einnahme an.<sup class="ref"><a href="#ref12">[12]</a></sup></p>
        <h2 id="use-disorder">Halluzinogenkonsumstörung</h2>
        <p>Das DSM-5 enthält die „Konsumstörung durch andere Halluzinogene“ (abgegrenzt von Phencyclidin), die diagnostiziert werden kann, wenn eine Person ein problematisches Gebrauchsmuster zeigt, zum Beispiel übermäßige Zeit mit Beschaffen oder Konsum verbringt, wichtige Aktivitäten aufgibt oder trotz Schaden fortfährt.<sup class="ref"><a href="#ref5">[5]</a></sup> Weil Toleranz als ein Kriterium zählt und Entzug nicht gilt, stützt sich die Diagnose vor allem auf Verhaltenskriterien. Die Prävalenz ist gering: das DSM-5 nennt eine 12-Monats-Prävalenz von etwa 0.1% unter Erwachsenen in den USA, und in behandlungssuchenden Populationen sind Halluzinogene selten die Hauptdroge.<sup class="ref"><a href="#ref5">[5]</a></sup><sup class="ref"><a href="#ref8">[8]</a></sup></p>
        <p>Warnzeichen, dass der Gebrauch problematisch geworden ist, ähneln denen jeder Substanz: häufiger gebrauchen als beabsichtigt, gebrauchen um dem Leben auszuweichen statt sich darauf einzulassen, Gebrauch, der Arbeit, Beziehungen oder Sicherheit stört, und Schwierigkeit aufzuhören, obwohl man es will. Da Psilocybin keine körperliche Abhängigkeit erzeugt, ist die angemessene Reaktion psychologische Unterstützung, nicht medizinische Entgiftung. Die National Helpline von SAMHSA (1-800-662-4357) bietet kostenlose, vertrauliche Vermittlungen.<sup class="ref"><a href="#ref13">[13]</a></sup></p>
        <h2 id="microdosing">Verändert Mikrodosierung das Bild?</h2>
        <p>Mikrodosierung, also subperzeptuelle Mengen alle paar Tage einzunehmen, ist das einzige Muster des Psilocybin-Gebrauchs, das absichtlich gewohnheitsmäßig ist. Auch hier ist Abhängigkeit im pharmakologischen Sinn nicht beobachtet worden, und die meisten Protokolle sehen Ruhetage gerade wegen der Toleranz vor.<sup class="ref"><a href="#ref14">[14]</a></sup> Die offenen Fragen zur Mikrodosierung betreffen die Wirksamkeit (placebokontrollierte Studien zeigen, dass die meisten berichteten Vorteile dem Placebo entsprechen) und das Fehlen langfristiger Sicherheitsdaten zur wiederholten Aktivierung von 5-HT<sub>2B</sub>-Rezeptoren, ein theoretisches Anliegen bezüglich der Herzklappen, nicht die Abhängigkeit.<sup class="ref"><a href="#ref14">[14]</a></sup><sup class="ref"><a href="#ref15">[15]</a></sup></p>
        <h2 id="treatment">Psilocybin als Behandlung der Abhängigkeit</h2>
        <p>Statt Abhängigkeit zu verursachen, wird Psilocybin als Behandlung dafür untersucht. In einer randomisierten Studie von 2022 an der NYU verringerten zwei überwachte Psilocybin-Sitzungen kombiniert mit Therapie die Tage starken Alkoholkonsums bei Menschen mit Alkoholkonsumstörung um 83% über acht Monate, gegenüber 51% mit einem aktiven Placebo.<sup class="ref"><a href="#ref16">[16]</a></sup> Eine Pilotstudie von Johns Hopkins zu Psilocybin zur Tabakentwöhnung berichtete 80% biologisch verifizierte Abstinenz nach sechs Monaten und 60% nach 30 Monaten, deutlich über den Raten herkömmlicher Behandlungen, obwohl die Studie klein und unkontrolliert war.<sup class="ref"><a href="#ref17">[17]</a></sup> Größere Studien zu Alkohol-, Tabak-, Opioid- und Kokainkonsumstörungen laufen.</p>
        <h2 id="harm-reduction">Schadensminderung</h2>
        <p>Weil das Abhängigkeitsrisiko gering ist, konzentriert sich die Schadensminderung bei Pilzen auf die akuten Risiken, die in <a href="/de/are-magic-mushrooms-dangerous/">Sind Zauberpilze gefährlich?</a> behandelt werden: Pilzbestimmung, Dosis, Setting, eine nüchterne Begleitperson und das Vermeiden von Kombinationen mit Lithium, Alkohol und Stimulanzien. Spezifisch für Gebrauchsmuster:</p>
        <ul>
            <li><strong>Setzen Sie Sitzungen auseinander.</strong> Toleranz bedeutet, dass erneute Einnahme innerhalb von Tagen weitgehend verschwendet ist und körperliche Anstrengung ohne Effekt hinzufügt. Viele erfahrene Konsumierende und klinisch Tätige schlagen Wochen oder Monate zwischen vollen Dosen vor.</li>
            <li><strong>Beachten Sie den Grund.</strong> Gebrauchen zum Erkunden, Feiern oder Verarbeiten ist etwas anderes als gebrauchen zum Ausweichen. Wenn Pilze zum Bewältigungsmittel für etwas geworden sind, braucht dieses Etwas weiterhin Aufmerksamkeit.</li>
            <li><strong>Achten Sie auf andere Substanzen.</strong> Menschen, die Probleme rund um Psychedelika entwickeln, haben häufig zugleich problematischen Alkohol- oder Cannabiskonsum; das sind gewöhnlich die Drogen, die zuerst angegangen werden müssen.</li>
            <li><strong>Die Vorgeschichte der psychischen Gesundheit wiegt schwerer als das Abhängigkeitsrisiko.</strong> Der Hauptgrund, beim wiederholten Gebrauch vorsichtig zu sein, ist psychiatrische Vulnerabilität, nicht Abhängigkeit.</li>
        </ul>
        <h2 id="see-also">Siehe auch</h2>
        <div class="see-also">
        <ul>
            <li><a href="/de/are-magic-mushrooms-dangerous/">Sind Zauberpilze gefährlich?</a>: Nebenwirkungen, Bad Trips, Überdosis und Wechselwirkungen</li>
            <li><a href="/de/">Psilocybin</a>: Überblick, Pharmakologie, Forschung und Rechtslage</li>
            <li><a href="/de/#therapeutic">Therapeutische Anwendungen</a>: Studien zu Substanzkonsumstörungen</li>
        </ul>
        </div>
<div class="ambox help">
            <strong>Wenn jemand jetzt Hilfe braucht:</strong> US Poison Control <strong>1-800-222-1222</strong> (24/7, kostenlos, vertraulich) &middot; Notruf <strong>911</strong> &middot; SAMHSA National Helpline <strong>1-800-662-4357</strong> &middot; Psychedelische Peer-Unterstützungshotline von Fireside Project <strong>62-FIRESIDE (623-473-7433)</strong> &middot; 988 Suicide &amp; Crisis Lifeline: anrufen oder eine Nachricht senden an <strong>988</strong>.
        </div>
        <h2 id="references">Quellen</h2>
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
            "title": "Psilocybin | WikiPsilocybin",
            "description": "WikiPsilocybin ist eine unabhängige Enzyklopädie zu Psilocybin-Forschung, klinischen Studien, rechtlichen Entwicklungen und Schadensminderung. Jede Aussage ist mit einer Primärquelle belegt.",
            "content": HOME_CONTENT,
            "extra_nav": True,
        },
        {
            "page": "/are-magic-mushrooms-dangerous/",
            "title": "Sind Zauberpilze gefährlich? Risiken, Nebenwirkungen und Sicherheit | WikiPsilocybin",
            "description": "Sind Zauberpilze gefährlich? Eine evidenzbasierte Übersicht der Risiken von Psilocybin: Nebenwirkungen, Bad Trips, Überdosis und Vergiftungssymptome, Wechselwirkungen, Kontraindikationen für die psychische Gesundheit und Schadensminderung. Vollständig mit Quellen belegt.",
            "content": DANGER_CONTENT,
            "extra_nav": False,
        },
        {
            "page": "/are-shrooms-addictive/",
            "title": "Machen Pilze abhängig? Abhängigkeit, Toleranz und Entzug | WikiPsilocybin",
            "description": "Machen Pilze abhängig? Was die Forschung zu Psilocybin-Abhängigkeit, Toleranz, Entzug und Halluzinogenkonsumstörung sagt, und warum Fachleute das Missbrauchspotenzial als gering einstufen. Vollständig mit Quellen belegt.",
            "content": ADDICTION_CONTENT,
            "extra_nav": False,
        },
    ]
    for spec in pages:
        html = render_page(
            lang="de",
            page=spec["page"],
            title=spec["title"],
            description=spec["description"],
            content=spec["content"],
            active_tab="article",
            extra_nav=spec["extra_nav"],
        )
        dest = write_page("de", spec["page"], html)
        print(f"wrote {dest}")


if __name__ == "__main__":
    main()
