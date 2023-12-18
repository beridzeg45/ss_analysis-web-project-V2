from imports import *

df=pd.read_csv('all_time_grouped.csv')
df['Date Published']=pd.to_datetime(df['Date Published'],errors='coerce')


grouped=df.groupby(['General Address','Status'])['Price Per SQMT'].median().reset_index().sort_values(['Price Per SQMT'],ascending=[False])


fig=px.bar(grouped,x='General Address',y='Price Per SQMT',
           color='Status',barmode='group',
           text=grouped['Price Per SQMT'].round().astype(int).astype(str)+' $',
)

fig.update_layout(height=600,template='plotly_dark')
fig.update_layout(title=dict(text='Median Apartment Prices Per SQMT By Month And City Part',font_family='Arial Black',font_size=15))
fig2=fig

print('Finished Figure_2')
