from sqlalchemy import MetaData, Table, Column, Integer, String, Date, Boolean, PrimaryKeyConstraint, ForeignKeyConstraint

meta = MetaData()


player = Table(
    'player', meta,
    Column('id',   Integer,     nullable=False),
    Column('name', String(100), nullable=False),
    Column('time', Integer, server_default="0", nullable=False),
    # Indexes #
    PrimaryKeyConstraint('id', name='player_id_pkey')
)


quest = Table(
    'quest', meta,
    Column('id',            Integer,      nullable=False),
    Column('quest_text',    String(1000), nullable=False),
    Column('pub_date',      Date,         nullable=False),
    Column('deadline',      Date,         nullable=True),
    Column('fulfilled',     Boolean,      default=False),
    Column('confirmation',  String(1000), nullable=True),
    Column('value',         Integer,      nullable=False),
    Column('player_id',     Integer,      nullable=False),
    Column('creator_id',    Integer,      nullable=False),
    # Indexes #
    PrimaryKeyConstraint('id', name='quest_id_pkey'),
    ForeignKeyConstraint(['player_id'], [player.c.id],
                     name='choice_player_id_fkey',
                     ondelete='CASCADE'),
    ForeignKeyConstraint(['creator_id'], [player.c.id],
                         name='choice_creator_id_fkey',
                         ondelete='CASCADE'),
)
