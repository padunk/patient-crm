from django import forms


class SearchForm(forms.Form):
    search_query = forms.CharField(
        label='', max_length=100, required=True,
        widget=forms.TextInput(
            attrs={'class': 'px-4 py-2 border border-gray-400 w-96 max-w-full rounded-md',
                   'placeholder': 'Search patient name or address',
                   'x-model': 'searchQuery',
                   })
    )
