from rest_framework import serializers
from app_api.models import StudentsModel, EmployeeModel, PersonModel, PlayerModel, Song, Singer

# validators examples
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with R.')
    


class StudentsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    roll = serializers.CharField(required=True, max_length=100)
    name = serializers.CharField(required=True, max_length=250, validators=[starts_with_r])
    mark = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
    details = serializers.CharField(required=False, max_length=500)

    def create(self, validated_data):
        return StudentsModel.objects.create(**validated_data)
    
    # feild level validations
    def validate_mark(self, value):
        if value <= 30:
            raise serializers.ValidationError("You have to input more then 30.")
        return value
    
    # object level validations
    def validate(self, data):
        roll = data.get('roll')
        name = data.get('name')

        if len(roll) >=5:
            raise serializers.ValidationError('You have to input low value.')
        
        if len(name) <=2:
            raise serializers.ValidationError('You have to input minimum three charecters.')
        
        return data
    

# Using HyperlinkedModelSerializer class
class StudentHyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='app_api:studentsmodel-detail')
    class Meta:
        model = StudentsModel
        fields = ['id', 'url', 'name', 'roll', 'mark', 'email', 'details']
    



class EmployeeSerializer(serializers.ModelSerializer):
    # validators examples
    def starts_with_t(value):
        if value[0].lower() != 't':
            raise serializers.ValidationError('Name should start with T.')

    name = serializers.CharField(required=True, max_length=250, validators=[starts_with_t])
    class Meta:
        model = EmployeeModel
        fields = ['id', 'name', 'position', 'salary', 'department']

        # read_only_fields = ['name', 'department']
        # extra_kwargs = {'name': {'write_only': True}}


        # feild level validations
    def validate_salary(self, value):
        if value <= 5000:
            raise serializers.ValidationError("Salary must be 5000 up.")
        return value
    
    # object level validations
    def validate(self, data):
        department = data.get('department')
        name = data.get('name')

        if len(department) <=3:
            raise serializers.ValidationError('You have to input minimum four charecters.')
        
        if len(name) <=2:
            raise serializers.ValidationError('You have to input minimum three charecters.')
        
        return data
    

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = ['id', 'name', 'age']
        extra_kwargs = {'name': {'required': True}, 'age': {'required': True}}



class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerModel
        fields = ['id', 'name', 'age']
        extra_kwargs = {'name': {'required': True}, 'age': {'required': True}}



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    # songs = serializers.StringRelatedField(many=True, read_only=True)
    # songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # songs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    # songs = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='app_api:song-detail')
    # songs = serializers.HyperlinkedIdentityField(view_name='app_api:song-detail')

    # Nested Serialize
    songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songs']