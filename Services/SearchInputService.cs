public class SearchInputService
{
    private string _text = string.Empty;
    
    public event Action OnTextChanged;
    
    public string Text
    {
        get => _text;
        set
        {
            _text = value;
            NotifyTextChanged();
        }
    }

    public void NotifyTextChanged() => OnTextChanged?.Invoke();
}