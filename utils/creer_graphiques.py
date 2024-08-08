import pandas as pd
import plotly.express as px

class ShiseidoGraphique:
   
    def __init__(self, shiseido_rep_age_usa, shiseido_rep_age_fr):
        self.shiseido_rep_age_usa = shiseido_rep_age_usa
        self.shiseido_rep_age_fr = shiseido_rep_age_fr
        
    
    def generer_graphique_repartition_avis_usa(self):
        repartition_avis = self.shiseido_rep_age_usa['pourcentage_repartition_avis']
        df_rep_avis_usa = pd.DataFrame(list(repartition_avis.items()), columns=['categorie_age', 'pourcentage'])
        
        fig = px.bar(df_rep_avis_usa,
             x='categorie_age', 
             y='pourcentage',
             color='categorie_age',
             text='pourcentage', 
             width=710, 
             height=480,
             color_discrete_map={'18-24': '#000000', 
                                 '25-34': '#CB5159',
                                 '35-44': '#73191F',
                                 '45-54':'#FFC4C8' ,
                                 '55-64': '#D6BCBD',
                                 '>65': '#B7757D',
                                 'sans age': '#B22334'
                                }
            
            )

        fig.update_layout(showlegend=False,
                plot_bgcolor='rgba(0, 0, 0, 0)',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                xaxis_title=None,
                yaxis_title=None,
                font_family="Verdana"
)

        fig.update_traces(textposition='outside',textfont_size=14, texttemplate='<b>%{y} % </b>')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)

        fig.write_image("graphique_usa.png")
        
        
        
    def generer_graphique_repartition_avis_fr(self):
            repartition_avis = self.shiseido_rep_age_fr['pourcentage_repartition_avis']
            df_rep_avis_fr = pd.DataFrame(list(repartition_avis.items()), columns=['categorie_age', 'pourcentage'])
            
            fig = px.bar(df_rep_avis_fr,
                x='categorie_age', 
                y='pourcentage',
                color='categorie_age',
                text='pourcentage', 
                width=710, 
                height=480,
                color_discrete_map={'18-24': '#000000', 
                                    '25-34': '#CB5159',
                                    '35-44': '#73191F',
                                    '45-54':'#FFC4C8' ,
                                    '55-64': '#D6BCBD',
                                    '>65': '#B7757D',
                                    'sans age': '#B22334'
                                    }
                
                )

            fig.update_layout(showlegend=False,
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    paper_bgcolor='rgba(0, 0, 0, 0)',
                    xaxis_title=None,
                    yaxis_title=None,
                    font_family="Verdana"
    )

            fig.update_traces(textposition='outside',textfont_size=14, texttemplate='<b>%{y} % </b>')
            fig.update_xaxes(showgrid=False, zeroline=False)
            fig.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)

            fig.write_image("graphique_fr.png")