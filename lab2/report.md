## 1. Introduktion
#### Denna rapport undersöker tolkningsbarhet i ett förtränat konvolutionellt neuralt nätverk (ResNet18) med hjälp av Grad-CAM (Class Activation Mapping). Syftet är att analysera vilka delar av en bild modellen fokuserar på när den gör sina klassificeringar, samt hur detta skiljer sig mellan korrekta och felaktiga prediktioner.

---

## 2. Metod
#### En förtränad ResNet18-modell tränad på ImageNet (1000 klasser) användes. Grad-CAM applicerades på det sista konvolutionella lagret (layer4) för att visualisera vilka bildregioner som påverkar modellens beslut mest.

#### Sex bilder testades:
#### - Tre positiva exempel: båt, blomma, stol
#### - Tre negativa exempel: val, TV, geting

#### För varje bild analyserades modellens prediktion samt dess aktiveringskarta (CAM).

---

## 3. Resultat och observationer

### 3.1 Båt (positivt exempel)
#### Modellen klassificerade bilden korrekt som en “speedboat”. CAM visar stark fokus på den centrala delen av båten, särskilt kanter och struktur. Detta tyder på att modellen använder relevanta objektbaserade egenskaper. 

---

### 3.2 Blomma (positivt exempel)
#### Blomman klassificerades korrekt som “daisy". Heatmap fokuserar främst på blomman och dess kronblad. Detta visar att modellen använder färg- och texturmönster för att känna igen objektet.

---

### 3.3 Stol (positivt exempel)
#### Modellen identifierade stolen korrekt. CAM visar fokus på stolens form och struktur, medan bakgrunden påverkar resultatet i mindre grad. 

---

### 3.4 Val (negativt exempel)
#### Valen klassificerades felaktigt som “great white shark”. Heatmap visar fokus på kroppens form och vattenmiljön, vilket tyder på att modellen förlitar sig på visuella likheter snarare än faktisk semantisk förståelse.

---

### 3.5 TV (negativt exempel)
#### TV-bilden klassificerades som "fire screen". Heatmap fokuserar främst på den rektangulära skärmytan och konturerna av objektet. Detta tyder på att modellen främst använder form och geometriska drag för klassificering snarare än faktisk förståelse av objektets funktion.

---

### 3.6 Geting (negativt exempel)
#### Getingen klassificerades felaktigt som en liknande insekt “lacewing”. Heatmap fokuserar på vingar och kroppsform, vilket visar att små och visuellt lika objekt är svårare att skilja åt.

---

## 4. Diskussion
#### Resultaten visar att det neurala nätverket inte “förstår” objekt på ett mänskligt sätt, utan istället baserar sina beslut på visuella egenskaper som form, färg och textur. Modellen är förtränad på ImageNet-datasetet som innehåller 1000 fasta klasser. Detta innebär att modellen endast kan klassificera bilder inom dessa fördefinierade kategorier. Om ett objekt inte finns representerat som en exakt klass i datasetet, kommer modellen istället att välja den klass som visuellt liknar objektet mest. Grad-CAM visar att korrekta klassificeringar ofta har tydligt fokus på objektet, medan felklassificeringar ofta bygger på mer generella visuella likheter.

---

## 5. Slutsats
#### Grad-CAM är ett effektivt verktyg för att tolka konvolutionella neurala nätverk. Det gör det möjligt att visualisera vilka delar av en bild som påverkar modellens beslut. Resultaten visar att modellen fungerar bra för tydliga objekt, men kan göra fel när olika klasser har visuella likheter.