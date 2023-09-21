import pandas as pd
import spacy

df = pd.read_csv('rising.csv')

nlp = spacy.load('en_core_web_sm')

# remove punctuations and store them
df['cleaned_text'] = df['text'].apply(lambda x: " ".join(
    token.text.lower() for token in nlp(str(x)) if not token.is_punct))

# keywords
flood_keywords = [
    'flood', 'flooding', 'flooded',
    'deluge', 'inundation', 'overflow',
    'flash flood', 'river flood', 'torrential rain',
    'natural disaster', 'emergency evacuation',
    'flood alert', 'levee', 'dam failure',
    'disaster relief', 'water damage', 'rising waters',
    'heavy rainfall', 'rainstorm', 'storm surge',
    'flash flood warning', 'flood risk',
    'floodwaters', 'flooded streets', 'evacuation orders',
    'flood recovery', 'flood victims', 'flood prevention',
    'flood management', 'flood insurance', 'flood forecast',
    'flood response', 'flood preparedness', 'flood recovery',
    'flood assistance', 'flood damage assessment', 'flood rescue',
    'flood relief efforts', 'flood-related deaths', 'flood response team',
    'flood warning system', 'flood-prone areas', 'flood emergency',
    'river overflow', 'flooded homes', 'rainfall intensity',
    'floodwaters rising', 'water levels', 'flood crisis',
    'flood response team', 'flood emergency plan', 'flood impact',
    'flood casualties', 'flood risk assessment', 'flood danger',
    'flood damage recovery', 'flood cleanup', 'flood resilience',
    'flood hazard', 'flood insurance claim', 'flash flood watch',
    'flood warning issued', 'evacuation shelters', 'flood barriers',
    'floodwater rescue', 'flood-damaged infrastructure', 'flood forecasting',
    'flood safety precautions', 'flood aftermath', 'flood recovery fund',
    'flooding in urban areas', 'riverbank erosion', 'rising river levels',
    'flood relief operations', 'flood mapping', 'monsoon floods',
    'historic flood', 'flood-affected communities', 'flood response coordination',
    'flood preparedness plan', 'damaged bridges', 'flood threat assessment',
    'flood monitoring', 'flood risk reduction', 'flood mitigation measures',
    'floodplain management', 'flood barrier construction', 'flood resilience programs'
]

water_scarcity_keywords = [
    'water scarcity', 'water shortage', 'lack of water',
    'drought', 'dry spell', 'water crisis',
    'limited water supply', 'water stress', 'depletion of water resources',
    'insufficient water', 'water rationing', 'water deficit',
    'water conservation', 'water management', 'water resources',
    'water supply issues', 'drought conditions', 'water crisis management',
    'water allocation', 'water use restrictions', 'water consumption',
    'water-saving measures', 'water conservation efforts', 'water access',
    'water infrastructure', 'water policy', 'water scarcity solutions',
    'sustainable water management', 'water scarcity impact', 'water scarcity assessment',
    'water scarcity mitigation', 'water scarcity adaptation', 'water scarcity challenges',
    'water scarcity in agriculture', 'water scarcity in urban areas', 'water scarcity in industry',
    'water scarcity in developing countries', 'water scarcity crisis', 'water scarcity awareness',
    'global water scarcity', 'water scarcity consequences', 'water scarcity prevention',
    'water scarcity planning', 'water scarcity strategies', 'water scarcity report',
    'water scarcity statistics', 'water scarcity trends', 'water scarcity effects',
    'water scarcity and climate change', 'water scarcity and population growth',
    'water crisis management', 'water scarcity impact assessment', 'water shortage solutions',
    'water scarcity challenges', 'water scarcity adaptation strategies', 'water scarcity awareness campaign',
    'water scarcity policy', 'water scarcity governance', 'water scarcity emergency response',
    'water scarcity resilience', 'water scarcity indicators', 'water scarcity vulnerability',
    'water scarcity risk assessment', 'water scarcity and food security', 'water scarcity and poverty',
    'water scarcity and economic development', 'water scarcity in arid regions', 'water scarcity in urban planning',
    'water scarcity in agriculture', 'water scarcity in industry', 'water scarcity in developing countries',
    'water scarcity and health', 'water scarcity and education', 'water scarcity and conflict',
    'water scarcity and migration', 'water scarcity and gender equality', 'water scarcity and sustainable development',
    'water scarcity and environmental impact', 'water scarcity and water conservation',
    'water scarcity and water recycling', 'water scarcity and water management',
    'water scarcity and freshwater ecosystems', 'water scarcity and groundwater depletion',
    'water scarcity and water technology', 'water scarcity and climate change adaptation',
    'water scarcity and global water governance', 'water scarcity and water rights', 'water scarcity and public policy',
    'water scarcity and international cooperation', 'water scarcity and humanitarian efforts',
    'water scarcity and disaster preparedness', 'water scarcity and community resilience',
    'water scarcity and corporate responsibility', 'water scarcity and sustainable agriculture'
]


drought_keywords = [
    'drought', 'dry spell', 'no rainfall',
    'prolonged drought', 'severe drought', 'water shortage',
    'crop failure', 'agricultural drought', 'hydrological drought',
    'meteorological drought', 'soil moisture deficit', 'water stress',
    'drinking water scarcity', 'drought conditions', 'drought impact',
    'drought mitigation', 'drought management', 'drought response',
    'drought relief', 'drought resilience', 'drought assessment',
    'drought monitoring', 'drought preparedness', 'drought declaration',
    'drought emergency', 'drought forecasting', 'drought recovery',
    'drought-stricken', 'drought crisis', 'drought vulnerability',
    'drought effects', 'drought adaptation', 'drought risk assessment',
    'drought-prone areas', 'drought-resistant crops', 'water conservation during drought',
    'water rationing during drought', 'drought in agriculture', 'drought in rural areas',
    'drought in urban areas', 'impact of drought on ecosystems', 'drought and food security',
    'drought and water resources', 'drought and climate change', 'drought and wildfires',
    'drought and heatwaves', 'drought and agriculture', 'drought and drinking water supply',
    'drought and environmental consequences', 'drought and economic impact', 'drought and migration',
    'drought and social implications', 'drought recovery efforts', 'drought relief initiatives',
    'drought management strategies', 'drought emergency response', 'drought risk reduction',
    'drought preparedness measures', 'drought early warning system', 'drought impact assessment',
    'drought resilience programs', 'sustainable drought management', 'community drought resilience',
    'drought policy and governance', 'drought and water conservation measures',
    'drought and water recycling', 'drought and groundwater depletion',
    'drought and water technology', 'drought and climate change adaptation',
    'drought and global water governance', 'drought and water rights', 'drought and public policy',
    'drought and international cooperation', 'drought and humanitarian efforts',
    'drought and disaster preparedness', 'drought and community resilience',
    'drought and corporate responsibility', 'drought and sustainable agriculture',
    'drought impact on water supply', 'drought and food production', 'drought and famine',
    'drought and soil erosion', 'drought and desertification', 'drought and ecosystem degradation',
    'drought and wildlife habitat', 'drought and biodiversity', 'drought and river flow',
    'drought and groundwater recharge', 'drought and water table', 'drought and water reservoirs',
    'drought and irrigation', 'drought and agricultural losses', 'drought and livestock',
    'drought and rural livelihoods', 'drought and migration', 'drought and conflict',
    'drought and social unrest', 'drought and economic impact', 'drought and water scarcity',
    'drought and climate adaptation', 'drought and disaster management', 'drought relief efforts',
    'drought assistance programs', 'drought recovery initiatives', 'drought resilience projects',
    'drought monitoring and early warning', 'drought response coordination', 'drought risk assessment',
    'drought vulnerability mapping', 'drought-prone regions', 'drought impact on water quality',
    'drought and waterborne diseases', 'drought and public health', 'drought and mental health',
    'drought and community support', 'drought preparedness training', 'drought and water conservation policies',
    'drought and water-efficient technologies', 'drought and sustainable land management',
    'drought and ecosystem restoration', 'drought and climate resilience', 'drought and indigenous knowledge',
    'drought and traditional water management', 'drought and disaster resilience', 'drought and water rights',
    'drought and international cooperation', 'drought and humanitarian aid', 'drought and community empowerment',
    'drought and gender equality', 'drought and education access',
    'drought and water governance', 'drought and policy advocacy', 'drought and research initiatives',
    'drought and corporate sustainability', 'drought and sustainable agriculture practices'
]

category_keywords = {
    'flood': flood_keywords,
    'water scarcity': water_scarcity_keywords,
    'drought': drought_keywords
}

city_category_list = []

for index, row in df.iterrows():
    text = row['cleaned_text']

    doc = nlp(text)

    # NER SPACY
    cities = [ent.text for ent in doc.ents if ent.label_ == 'GPE']

    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in text:
                for city in cities:
                    city_category_list.append((city, category))

# Create a df
city_keyword = pd.DataFrame(
    city_category_list, columns=['city', 'category'])

# Save the results to a CSV file
city_keyword.to_csv(
    'city_keyword_category_results.csv', index=False)
